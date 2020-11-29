import os
from typing import Tuple, Generator, Dict

from pyUbiForge2.api.data_types import (
    DataFileIdentifier,
    FileIdentifier,
    FileResourceType,
    FileName,
    DataFileStorage,
    DataFileByteLocations,
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
        raise NotImplementedError

    def _parse_forge(self) -> DataFileByteLocations:
        """Parse the forge file to load metadata and data file locations."""
        raise NotImplementedError

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

    def _decompress_data_file(self, compressed_bytes: bytes) -> bytes:
        """Decompress the raw data file bytes.

        :param compressed_bytes: The bytes of the data file as they appear on disk
        :return: The decompressed bytes of the data file
        """
        raise NotImplementedError

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
        if data_file_id in self.NonContainerDataFiles:
            raw_data = self.get_compressed_data_file(data_file_id)
            return {
                data_file_id: (0, "", raw_data)
            }
        else:
            decompressed_data = self.get_decompressed_data_file(data_file_id)
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
