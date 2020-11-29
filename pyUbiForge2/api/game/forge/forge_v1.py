import os
from typing import Tuple, Generator, Dict, Optional, List
import gzip
import pickle
import traceback
import numpy
import struct
from io import BytesIO

from .forge import BaseForge
from pyUbiForge2 import CACHE_DIR
from pyUbiForge2.api import log
from pyUbiForge2.api.data_types import (
    FileIdentifier,
    FileResourceType,
    FileName,
    FileStorage,
    SerialisedMetadata,
    DataFileByteLocations,
    DataFileMetadata,
)
from pyUbiForge2.api.game.data_file import DataFile
from pyUbiForge2.util.compression import decompress


class BaseForgeV1(BaseForge):
    """The base API for a forge file. Each game should build from this."""

    NonContainerDataFiles = {16, 145}
    CompressionMarker = b'\x33\xAA\xFB\x57\x99\xFA\x04\x10'
    DataFileFormat = 0  # 0=[AC1], 1=[AC2, AC2B, AC2R, ?], 3=[AC3L, ACRo], 4=[ACU]

    def init_iter(self) -> Generator[float, None, None]:
        """Load the metadata and populate DataFile classes.
        Yield back the progress on a scale from 0.0 to 1.0."""

        # get the data file metadata
        metadata, self._data_file_location = self._parse_forge()

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
            log.info(f"Decompressing {self.forge_name}.")
            database = {}
            index = 1
            for data_file_id, (data_file_resource_type, data_file_name) in metadata.items():
                # data_file = self._data_files[data_file_id] = DataFile(data_file_id, data_file_resource_type, data_file_name)
                try:
                    files = self.get_decompressed_files(data_file_id)
                except:
                    traceback.print_exc()
                    print(f"Error loading {self.file_name} {data_file_id} {data_file_name}")
                    continue
                assert data_file_id in files
                # in some cases the info will be in the index but not the data file (non archive formats)
                # and in some cases the info will be in the data file but not the index (Brotherhood is the first game I can see with data file id in the index)
                data_file_resource_type = data_file_resource_type or files[data_file_id][0]
                data_file_name = data_file_name or files[data_file_id][1]
                file_storage: FileStorage = {
                    file_id: (file_resource_type, file_name) for file_id, (file_resource_type, file_name, _) in files.items()
                }
                file_storage[data_file_id] = (data_file_resource_type, data_file_name)

                database[data_file_id] = (
                    data_file_resource_type,
                    data_file_name,
                    file_storage
                )
                yield index / len(metadata)
                index += 1
            os.makedirs(os.path.dirname(database_path), exist_ok=True)
            with gzip.open(database_path, 'wb') as f:
                pickle.dump(database, f)
            log.info(f"Finished decompressing {len(metadata)} data files.")

        log.info(f"Setting up database for {self.forge_name}.")
        for data_file_id, (data_file_resource_type, data_file_name, file_storage) in database.items():
            self._data_files[data_file_id] = DataFile(
                data_file_id,
                data_file_resource_type,
                data_file_name,
                file_storage
            )

        # populate
        yield 1.0

    def _parse_forge(self) -> Tuple[
        DataFileMetadata,
        DataFileByteLocations
    ]:
        """Parse the forge file to load metadata and data file locations."""
        log.info(f'Reading metadata from {self.forge_name}.')

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
                    ('raw_data_size', numpy.uint32),  # This is sometimes larger than the other size. The format of these is slightly different
                    ('', numpy.uint64),
                    ('', numpy.uint32),
                    ('file_type', numpy.uint32),  # sometimes file type
                    ('', numpy.uint64),
                    ('', numpy.uint32),  # next file count
                    ('', numpy.uint32),  # previous file count
                    ('', numpy.uint32),
                    ('', numpy.uint32),  # timestamp
                    ('data_file_name', 'S128'),  # usually data file name
                ] + [('', numpy.uint32)] * (5 if forge_file_version >= 27 else 4),
                index_count
            )
            # assert numpy.array_equal(index_table['raw_data_size'], name_table['raw_data_size']), "The duplicated raw data sizes do not match"
            # TODO: the above sometimes do not match in games before Unity (they all match in Unity). There seems to be more compressed data after this if that is the case.

            data_file_names = name_table["data_file_name"].astype(str)
            return dict(zip(
                index_table["file_id"],
                zip(name_table["file_type"].tolist(), data_file_names)
            )), dict(zip(
                index_table["file_id"],
                zip(
                    index_table["raw_data_offset"].tolist(),
                    index_table["raw_data_size"].tolist()
                )
            ))

    def _read_compressed_data_section(self, raw_data_chunk: BytesIO, exhaust=True) -> Tuple[int, List[bytes]]:
        """This is a helper function used in decompression"""
        raw_data_chunk.seek(2, 1)  # 01 00
        compression_type = ord(raw_data_chunk.read(1))
        raw_data_chunk.seek(2, 1)  # 00 80
        max_size = struct.unpack("<H", raw_data_chunk.read(2))[0]
        uncompressed_data_list = []
        if max_size:
            if self.DataFileFormat <= 2:
                comp_block_count = struct.unpack(
                    "<H",
                    raw_data_chunk.read(2)
                )[0]
            else:
                comp_block_count = struct.unpack(
                    "<I",
                    raw_data_chunk.read(4)
                )[0]
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
                    if self.DataFileFormat <= 2:  # this might be wrong
                        size = struct.unpack(
                            "<H",
                            raw_data_chunk.read(2)
                        )[0]
                    else:
                        size = struct.unpack(
                            "<I",
                            raw_data_chunk.read(4)
                        )[0]
                    uncompressed_data_list.append(raw_data_chunk.read(size))
                elif compressed == b"\x01":
                    compressed_size, uncompressed_size, _ = struct.unpack("<3I", raw_data_chunk.read(12))
                    uncompressed_data_list.append(decompress(compression_type, raw_data_chunk.read(compressed_size), uncompressed_size))
                else:
                    raise Exception(f"Extra metadata byte {compressed} is not recognised")
                if not exhaust:
                    break
                pointer = raw_data_chunk.tell()

        return max_size, uncompressed_data_list

    def _decompress_data_file(self, compressed_bytes: bytes) -> bytes:
        """Decompress the raw data file bytes.

        :param compressed_bytes: The bytes of the data file as they appear on disk
        :return: The decompressed bytes of the data file
        """
        uncompressed_data_list = []

        raw_data_chunk = BytesIO(compressed_bytes)
        if self.DataFileFormat == 1:
            raw_data_chunk.seek(4, 1)
        elif self.DataFileFormat == 2:
            raw_data_chunk.seek(4, 1)
            count = struct.unpack("<H", raw_data_chunk.read(2))[0]
            for _ in range(count):
                count2 = struct.unpack("<H", raw_data_chunk.read(2))[0]
                for _ in range(count2):
                    assert raw_data_chunk.read(1) == b"\x00"
                    raw_data_chunk.seek(8, 1)  # (data?) file id

            count = struct.unpack("<H", raw_data_chunk.read(2))[0]
            for _ in range(count):
                raw_data_chunk.seek(8, 1)  # (data?) file id
                raw_data_chunk.seek(1, 1)
                count2 = struct.unpack("<H", raw_data_chunk.read(2))[0]
                raw_data_chunk.seek(count2 * 2, 1)

        header = raw_data_chunk.read(8)
        if header == self.CompressionMarker:  # if compressed
            max_size, uncompressed_data_list = self._read_compressed_data_section(raw_data_chunk)
            if max_size:
                if raw_data_chunk.read(8) == self.CompressionMarker:
                    _, uncompressed_data_list_ = self._read_compressed_data_section(raw_data_chunk)
                    uncompressed_data_list += uncompressed_data_list_
                else:
                    raise Exception('Compression Issue. Second compression block not found')
            extra = raw_data_chunk.read()
            if extra:
                raise Exception('Compression Issue. More data found')
        else:
            raw_data_chunk_rest = header + raw_data_chunk.read()
            if self.CompressionMarker in raw_data_chunk_rest:
                raise Exception('Compression Issue')
            uncompressed_data_list.append(raw_data_chunk_rest)  # The file is not compressed

        return b''.join(uncompressed_data_list)

    def _unpack_decompressed_data_file(self, decompressed_bytes: bytes) -> Dict[
        FileIdentifier,
        Tuple[
            FileResourceType,
            FileName,
            bytes
        ]
    ]:
        files = {}
        uncompressed_data = BytesIO(decompressed_bytes)

        file_count = struct.unpack("<H", uncompressed_data.read(2))[0]
        if self.DataFileFormat == 0:
            index_table = [struct.unpack('<II', uncompressed_data.read(8)) for _ in range(file_count)]
        else:
            if self.DataFileFormat == 1:
                fmt = "<IIH"
            elif 2 <= self.DataFileFormat <= 3:
                fmt = "<QIH"
            else:
                raise Exception
            fmt_len = struct.calcsize(fmt)
            index_table = []
            for _ in range(file_count):
                index_table.append(
                    struct.unpack(fmt, uncompressed_data.read(fmt_len))
                )  # file_id, data_size (file_size + header), extra16_count (for next line)
                uncompressed_data.seek(index_table[-1][2] * 2, 1)
        for index in range(file_count):
            file_type, file_size, file_name_size = struct.unpack('<3I', uncompressed_data.read(12))
            file_id = index_table[index][0]
            file_name = uncompressed_data.read(file_name_size).decode("utf-8")
            check_byte = ord(uncompressed_data.read(1))
            if check_byte == 1:
                uncompressed_data.seek(3, 1)
                unk_count = struct.unpack("<I", uncompressed_data.read(4))[0]
                uncompressed_data.seek(12 * unk_count, 1)
            elif check_byte != 0:
                raise Exception('Either something has gone wrong or a new value has been found here')

            raw_file = uncompressed_data.read(file_size)

            files[file_id] = (file_type, file_name, raw_file)
        return files


class ForgeV1a(BaseForgeV1):
    """Used in AC1"""
    DataFileFormat = 0


class ForgeV1b(BaseForgeV1):
    """Used in AC2 to ?"""
    DataFileFormat = 1


class ForgeV1c(BaseForgeV1):
    """Used in ?"""
    DataFileFormat = 2


class ForgeV1d(BaseForgeV1):
    DataFileFormat = 3
