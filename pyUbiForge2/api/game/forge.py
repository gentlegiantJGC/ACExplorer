import os
from typing import Tuple, Generator, Dict, Optional
import gzip
import pickle
import traceback
import numpy
import struct

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


class BaseForge:
    """The base API for a forge file. Each game should build from this."""

    NonContainerDataFiles = set()

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
                    ('', numpy.uint32) * (5 if forge_file_version >= 27 else 4)
                ],
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
        offset, size = self._data_file_location[data_file_id]
        with open(self.path, 'rb') as f:
            f.seek(offset)
            return f.read(size)

    def get_decompressed_data_file(
            self,
            data_file_id: DataFileIdentifier
    ) -> bytes:
        """Decompress and return data for a given data file as a single block of bytes."""
        # Start byte and offset can be found in self._data_file_location
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
        Use get_decompressed_files_bytes to get just the bytes."""
        raise NotImplementedError

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
