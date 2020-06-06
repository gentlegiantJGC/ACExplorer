import os
from typing import Tuple, Generator, Dict, Optional
import gzip
import pickle
import traceback

from pyUbiForge2 import CACHE_DIR
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
from .data_file import DataFile


class BaseForge:
    """The base API for a forge file. Each game should build from this."""

    GameIdentifier = None  # string identifier to match the one used in the game class
    NonContainerDataFiles = set()

    def __init__(self, path: str):
        if self.__class__ is BaseForge:
            raise Exception("BaseForge must be subclassed")
        if self.GameIdentifier is None:
            raise Exception(f"GameIdentifier has not been set in {self.__class__.__name__}")
        self._path = path
        self._file_name = os.path.basename(path)
        self._forge_name = os.path.splitext(self._file_name)[0]

        self._file_size = os.path.getsize(path)

        self._data_file_location: DataFileByteLocations = {}
        self._data_files: DataFileStorage = {}

    def __repr__(self):
        return f"{self.GameIdentifier}:{self.file_name}"

    def init_iter(self) -> Generator[float, None, None]:
        """Load the metadata and populate DataFile classes.
        Yield back the progress on a scale from 0.0 to 1.0."""

        # get the data file metadata
        metadata, byte_locations = self._parse_forge()
        self._data_file_location.update(byte_locations)

        database_path = os.path.join(CACHE_DIR, self.GameIdentifier, f"{self.forge_name}.forge_db")
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
        raise NotImplementedError

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
