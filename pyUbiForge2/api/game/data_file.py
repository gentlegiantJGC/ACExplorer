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
    def __init__(
            self,
            data_file_id: DataFileIdentifier,
            resource_type: DataFileResourceType,
            name: DataFileName,
            files: FileStorage = None
    ):
        self.data_file_id = data_file_id
        self.resource_type = resource_type
        self.name = name
        self._files: FileStorage = files or {}

    def __repr__(self):
        return f"{self.name} {self.data_file_id} {self.resource_type:08X}"

    def __contains__(self, file_id: FileIdentifier):
        return file_id in self._files

    @property
    def files(self) -> FileStorage:
        return self._files

    @files.setter
    def files(self, files: FileStorage):
        self._files = files

    @property
    def file_ids(self) -> Tuple[FileIdentifier, ...]:
        return tuple(self._files.keys())

    def get_file(self, file_id: FileIdentifier) -> FileMetadata:
        return self._files[file_id]
