from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('B8C1681D')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(2)
        count = file.read_uint_32()
        for _ in range(count):
            file.read_bytes(2)
            file.read_file()
        count2 = file.read_uint_32()
        for _ in range(count2):
            file.read_bytes(1)
            file.read_file_id()
        count3 = file.read_uint_32()
        for _ in range(count3):
            file.read_uint_16()
