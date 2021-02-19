from typing import Tuple

from pyUbiForge2.api.data_types import (
    DataFileIdentifier,
    DataFileResourceType,
    DataFileName,
    FileStorage,
    FileIdentifier,
    FileMetadata,
)


class DataFile:
    __slots__ = ("_data_file_id", "_resource_type", "_name", "_files")
    def __init__(
            self,
            data_file_id: DataFileIdentifier,
            resource_type: DataFileResourceType,
            name: DataFileName,
            files: FileStorage
    ):
        self._data_file_id = data_file_id
        self._resource_type = resource_type
        self._name = name
        self._files: FileStorage = files

    @property
    def data_file_id(self) -> DataFileIdentifier:
        return self._data_file_id

    @property
    def resource_type(self) -> DataFileResourceType:
        return self._resource_type

    @property
    def name(self) -> DataFileName:
        return self._name

    def __repr__(self):
        return f"{self.name} {self.data_file_id} {self.resource_type:08X}"

    def __contains__(self, file_id: FileIdentifier):
        return file_id in self._files

    @property
    def files(self) -> FileStorage:
        """{file_id(int): (resource_type(int), file_name)}
        A dictionary converting file_id to a tuple of resource type and file name

        :return:
        """
        return self._files.copy()

    @property
    def file_ids(self) -> Tuple[FileIdentifier, ...]:
        return tuple(self._files.keys())

    def get_file(self, file_id: FileIdentifier) -> FileMetadata:
        return self._files[file_id]
