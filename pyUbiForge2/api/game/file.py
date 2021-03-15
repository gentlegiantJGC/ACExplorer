from abc import ABC, abstractmethod
from pyUbiForge2.api.file_object import FileDataWrapper


class BaseFile(ABC):
    ResourceType: int = None
    _file_id: int

    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        self._file_id = file_id

    @classmethod
    def from_data(
            cls,
            file_id: int,
            file: FileDataWrapper
    ):
        self = cls(file_id, file)
        self.load_from(file)

    @abstractmethod
    def load_from(self, file: FileDataWrapper):
        ...

    @property
    def file_id(self) -> int:
        """The file id of the file in question"""
        return self._file_id

    @property
    def resource_type(self) -> int:
        """The file resource type of the file in question"""
        return self.ResourceType


class SubclassBaseFile(BaseFile, ABC):
    ParentResourceType: int = None
    _parent: BaseFile

    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        self._parent = file.get_parser(self.ParentResourceType)(file_id, file)

    @property
    def parent(self) -> BaseFile:
        return self._parent
