from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('4661AAEF')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(2)
        count1 = file.read_uint_32()
        file.read_bytes(2 * count1)
        file.read_bytes(4 * 6)  # 6 floats
        count2 = file.read_uint_32()
        for _ in range(count2):
            file.read_bytes(24)
        file.read_bytes(1)
        file.out_file_write('\n')
