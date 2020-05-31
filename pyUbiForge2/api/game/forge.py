import os
from typing import Dict, Tuple, Generator

from pyUbiForge2.api.data_types import (
    DataFileIdentifier,
    DataFileResource,
    DataFileName,
    FileIdentifier,
    FileResource,
    FileName,
    DataFileStorage,
)
from .data_file import DataFile


class BaseForge:
    """The base API for a forge file. Each game should build from this."""
    def __init__(self, path: str):
        if self.__class__ is BaseForge:
            raise Exception("BaseForge must be subclassed")
        self._path = path
        self._file_name = os.path.basename(path)
        self._name = os.path.splitext(self._file_name)[0]

        self._file_size = os.path.getsize(path)

        self._data_files: DataFileStorage = {}

    def init_iter(self) -> Generator[float, None, None]:
        """Load the metadata and populate DataFile classes.
        Yield back the progress on a scale from 0.0 to 1.0."""
        # if the cache file exists load and populate with that
        # if not decompress the forge file, save the cache file and populate

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
        return self._name

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

    def get_data_file(self, data_file: DataFileIdentifier) -> DataFile:
        """Get the DataFile class for a given id.
        Will raise KeyError if the DataFile does not exist."""
        return self._data_files[data_file]
