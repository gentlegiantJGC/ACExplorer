from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('59327905')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        assert file.read_uint_8() == 0, "check byte failed"
        file.read_file_id()
        for _ in range(file.read_uint_32()):
            file.read_file()
        file.read_bytes(20)
