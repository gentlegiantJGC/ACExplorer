class BaseFile:
    def __init__(
            self,
            file_id: int,
            resource_type: int
    ):
        self._file_id = file_id
        self._resource_type = resource_type

    @property
    def file_id(self) -> int:
        """The file id of the file in question"""
        return self._file_id

    @property
    def resource_type(self) -> int:
        """The file resource type of the file in question"""
        return self._resource_type
