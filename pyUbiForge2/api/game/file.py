from pyUbiForge2.api.file_object import FileDataWrapper


class BaseFile:
    ResourceType: int = None

    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        self._file_id = file_id

    @property
    def file_id(self) -> int:
        """The file id of the file in question"""
        return self._file_id

    @property
    def resource_type(self) -> int:
        """The file resource type of the file in question"""
        return self.ResourceType
