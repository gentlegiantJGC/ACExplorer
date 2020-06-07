from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('414FF9F7')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(1)
        count1 = file.read_uint_32()
        for _ in range(count1):
            file.read_bytes(2)
            file.read_file_id()
            file.read_type()
            file.read_bytes(4)
            file.out_file_write('\n')
        file.out_file_write('\n')
