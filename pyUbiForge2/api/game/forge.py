import os
from typing import Tuple, Generator, Dict, Optional, List
import gzip
import pickle
import traceback
import numpy
import struct
from io import BytesIO

from pyUbiForge2 import CACHE_DIR
from pyUbiForge2.api import log
from pyUbiForge2.api.data_types import (
    DataFileIdentifier,
    FileIdentifier,
    FileResourceType,
    FileName,
    DataFileStorage,
    SerialisedMetadata,
    DataFileByteLocations,
    DataFileMetadata
)
from pyUbiForge2.api.game.data_file import DataFile
from pyUbiForge2.util.compression import decompress


class BaseForge:
    """The base API for a forge file. Each game should build from this."""

    NonContainerDataFiles = set()
    CompressionMarker = b'\x33\xAA\xFB\x57\x99\xFA\x04\x10'

    def __init__(self, game_identifier: str, path: str):
        if self.__class__ is BaseForge:
            raise Exception("BaseForge must be subclassed")
        self._game_identifier = game_identifier
        self._path = path
        self._file_name = os.path.basename(path)
        self._forge_name = os.path.splitext(self._file_name)[0]

        self._file_size = os.path.getsize(path)

        self._data_file_location: DataFileByteLocations = {}
        self._data_files: DataFileStorage = {}

    def __repr__(self):
        return f"{self.game_identifier}:{self.file_name}"

    def init_iter(self) -> Generator[float, None, None]:
        """Load the metadata and populate DataFile classes.
        Yield back the progress on a scale from 0.0 to 1.0."""

        # get the data file metadata
        metadata, byte_locations = self._parse_forge()
        self._data_file_location.update(byte_locations)

        database_path = os.path.join(CACHE_DIR, self.game_identifier, f"{self.forge_name}.forge_db")
        database: Optional[SerialisedMetadata]

        # load the saved database if it exists.
        if os.path.isfile(database_path):
            try:
                with gzip.open(database_path) as f:
                    database = pickle.load(f)
            except:
                database = None
        else:
            database = None

        # if it doesn't exist, decompile everything to build it
        if database is None:
            database = {}
            index = 0
            for data_file_id, (data_file_resource_type, data_file_name) in metadata.items():
                index += 1
                data_file = self._data_files[data_file_id] = DataFile(data_file_id, data_file_resource_type, data_file_name)
                try:
                    files = self.get_decompressed_files(data_file_id)
                except:
                    traceback.print_exc()
                    print(f"Error loading {self.file_name} {data_file_id} {data_file_name}")
                    files = {}
                database[data_file_id] = data_file.files = {
                    file_id: (file_resource_type, file_name) for file_id, (file_resource_type, file_name, _) in files.items()
                }
                yield index / len(metadata)
            os.makedirs(os.path.dirname(database_path), exist_ok=True)
            with gzip.open(database_path, 'wb') as f:
                pickle.dump(database, f)

        else:
            for data_file_id, (data_file_resource_type, data_file_name) in metadata.items():
                files = database.get(data_file_id, {})
                self._data_files[data_file_id] = DataFile(
                    data_file_id,
                    data_file_resource_type,
                    data_file_name,
                    files
                )

        # populate
        yield 1.0

    def _parse_forge(self) -> Tuple[
        DataFileMetadata,
        DataFileByteLocations
    ]:
        """Parse the forge file to load metadata and data file locations."""
        log.info(f'Building file tree for {self.forge_name}')

        with open(self.path, 'rb') as forge_file:
            # header
            if forge_file.read(8) != b'scimitar':
                return {}, {}
            forge_file.seek(1, 1)
            forge_file_version, file_data_header_offset = struct.unpack('<iQ', forge_file.read(12))
            if not 25 <= forge_file_version <= 27:
                raise Exception(f'Unsupported Forge file format : "{forge_file_version}"')
            if forge_file_version < 27:
                forge_file.seek(file_data_header_offset + 32)
            else:
                forge_file.seek(file_data_header_offset + 36)
            file_data_offset = struct.unpack('<q', forge_file.read(8))[0]
            forge_file.seek(file_data_offset)
            # File Data
            index_count, index_table_offset, file_data_offset2, name_table_offset, raw_data_table_offset = struct.unpack('<i4x2q8x2q', forge_file.read(48))
            forge_file.seek(index_table_offset)
            index_table: numpy.ndarray = numpy.fromfile(
                forge_file,
                [
                    ('raw_data_offset', numpy.uint64),
                    ('file_id', numpy.uint64 if forge_file_version >= 27 else numpy.uint32),
                    ('raw_data_size', numpy.uint32)
                ],
                index_count
            )
            if forge_file_version == 25:
                # there is a header here with not that much useful data
                index_table["raw_data_offset"] += 440

            forge_file.seek(name_table_offset)
            name_table: numpy.ndarray = numpy.fromfile(
                forge_file,
                [
                    ('raw_data_size', numpy.uint32),
                    ('', numpy.uint64),
                    ('', numpy.uint32),
                    ('file_type', numpy.uint32),
                    ('', numpy.uint64),
                    ('', numpy.uint32),  # next file count
                    ('', numpy.uint32),  # previous file count
                    ('', numpy.uint32),
                    ('', numpy.uint32),  # timestamp
                    ('file_name', 'S128'),
                ] + [('', numpy.uint32)] * (5 if forge_file_version >= 27 else 4),
                index_count
            )
            assert numpy.array_equal(index_table['raw_data_size'], name_table['raw_data_size']), "The duplicated raw data sizes do not match"

            file_names = name_table["file_name"].astype(str)
            return dict(zip(
                index_table["file_id"],
                zip(name_table["file_type"].tolist(), file_names)
            )), dict(zip(
                index_table["file_id"],
                index_table[["raw_data_offset", "raw_data_size"]].tolist()
            ))

    def get_compressed_data_file(
            self,
            data_file_id: DataFileIdentifier
    ) -> bytes:
        """Get the compressed packaged binary data of the data file as it appears on disk.

        :param data_file_id: The numerical id of the data file
        :return: The bytes as they appear on disk
        """
        offset, size = self._data_file_location[data_file_id]
        with open(self.path, 'rb') as f:
            f.seek(offset)
            return f.read(size)

    @staticmethod
    def _read_compressed_data_section(raw_data_chunk: BytesIO) -> Tuple[int, List[bytes]]:
        """This is a helper function used in decompression"""
        raw_data_chunk.seek(2, 1)  # 01 00
        compression_type = ord(raw_data_chunk.read(1))
        raw_data_chunk.seek(2, 1)  # 00 80
        max_size = struct.unpack("<H", raw_data_chunk.read(2))[0]
        uncompressed_data_list = []
        if max_size:
            comp_block_count = struct.unpack("<I", raw_data_chunk.read(4))[0]
            size_table = numpy.frombuffer(raw_data_chunk.read(comp_block_count * 2 * 2), '<u2').reshape(-1, 2).tolist()  # 'uncompressed_size', 'compressed_size'
            for uncompressed_size, compressed_size in size_table:
                raw_data_chunk.seek(4, 1)  # I think this is the hash of the data
                uncompressed_data_list.append(decompress(compression_type, raw_data_chunk.read(compressed_size), uncompressed_size))
        else:
            pointer = raw_data_chunk.tell()
            end_pointer = raw_data_chunk.seek(0, 2)
            raw_data_chunk.seek(pointer)

            while pointer < end_pointer:
                compressed = raw_data_chunk.read(1)
                if compressed == b"\x00":
                    size = struct.unpack("<I", raw_data_chunk.read(4))[0]
                    uncompressed_data_list.append(raw_data_chunk.read(size))
                elif compressed == b"\x01":
                    compressed_size, uncompressed_size, _ = struct.unpack("<3I", raw_data_chunk.read(12))
                    uncompressed_data_list.append(decompress(compression_type, raw_data_chunk.read(compressed_size), uncompressed_size))
                else:
                    raise Exception(f"Extra metadata byte {compressed} is not recognised")
                pointer = raw_data_chunk.tell()

        return max_size, uncompressed_data_list

    def _decompress_data_file(self, compressed_bytes: bytes) -> bytes:
        """Decompress the raw data file bytes.

        :param compressed_bytes: The bytes of the data file as they appear on disk
        :return: The decompressed bytes of the data file
        """
        uncompressed_data_list = []

        raw_data_chunk = BytesIO(compressed_bytes)
        header = raw_data_chunk.read(8)
        if header == self.CompressionMarker:  # if compressed
            max_size, uncompressed_data_list = self._read_compressed_data_section(raw_data_chunk)
            if max_size:
                if raw_data_chunk.read(8) == self.CompressionMarker:
                    _, uncompressed_data_list_ = self._read_compressed_data_section(raw_data_chunk)
                    uncompressed_data_list += uncompressed_data_list_
                else:
                    raise Exception('Compression Issue. Second compression block not found')
            if raw_data_chunk.read():
                raise Exception('Compression Issue. More data found')
        else:
            raw_data_chunk_rest = header + raw_data_chunk.read()
            if self.CompressionMarker in raw_data_chunk_rest:
                raise Exception('Compression Issue')
            uncompressed_data_list.append(raw_data_chunk_rest)  # The file is not compressed

        return b''.join(uncompressed_data_list)

    def get_decompressed_data_file(
            self,
            data_file_id: DataFileIdentifier
    ) -> bytes:
        """Decompress and return data for a given data file as a single block of bytes.

        :param data_file_id: The numerical id of the data file
        :return: The decompressed bytes
        """
        # Start byte and offset can be found in self._data_file_location
        return self._decompress_data_file(self.get_compressed_data_file(data_file_id))

    def _unpack_decompressed_data_file(self, decompressed_bytes: bytes) -> Dict[
        FileIdentifier,
        Tuple[
            FileResourceType,
            FileName,
            bytes
        ]
    ]:
        raise NotImplementedError

    def get_decompressed_files(self, data_file_id: DataFileIdentifier) -> Dict[
        FileIdentifier,
        Tuple[
            FileResourceType,
            FileName,
            bytes
        ]
    ]:
        """Get the data file unpacked into its individual files.
        This is a dictionary that converts from the file id to the metadata and file bytes.
        Use get_decompressed_files_bytes to get just the bytes.

        :param data_file_id:
        :return:
        """
        decompressed_data = self.get_decompressed_data_file(data_file_id)
        if data_file_id in self.NonContainerDataFiles:
            data_file = self.get_data_file(data_file_id)
            return {
                data_file_id: (data_file.resource_type, data_file.name, decompressed_data)
            }

        else:
            return self._unpack_decompressed_data_file(decompressed_data)

    def get_decompressed_files_bytes(self, data_file_id: DataFileIdentifier) -> Dict[
        FileIdentifier,
        bytes
    ]:
        """Get the bytes for each file in a given data file.
        This is a dictionary that converts from the file id to file bytes."""
        return {file_id: data[2] for file_id, data in self.get_decompressed_files(data_file_id).items()}

    @property
    def game_identifier(self):
        """The identifier for the game this forge file is associated with."""
        return self._game_identifier

    @property
    def path(self) -> str:
        """The full path where the forge file is located.
        eg .../Ubisoft Game Launcher/games/Assassin's Creed Unity/DataPC_ACU_Paris.forge"""
        return self._path

    @property
    def file_name(self) -> str:
        """The file name of the forge file.
        eg DataPC_ACU_Paris.forge"""
        return self._file_name

    @property
    def forge_name(self) -> str:
        """The identifier name of the forge file.
        eg DataPC_ACU_Paris"""
        return self._forge_name

    @property
    def file_size(self) -> int:
        """The size of the forge file in bytes"""
        return self._file_size

    @property
    def data_files(self) -> DataFileStorage:
        """A dictionary of data file ids and the corresponding DataFile class."""
        return self._data_files

    @property
    def data_file_ids(self) -> Tuple[DataFileIdentifier, ...]:
        """A tuple of data file ids contained within this forge file."""
        return tuple(self._data_files.keys())

    def get_data_file(self, data_file_id: DataFileIdentifier) -> DataFile:
        """Get the DataFile class for a given id.
        Will raise KeyError if the DataFile does not exist."""
        return self._data_files[data_file_id]
