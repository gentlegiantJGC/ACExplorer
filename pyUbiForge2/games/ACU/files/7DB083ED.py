from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('7DB083ED')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(26)
        check_byte = file.read_uint_8()
        if check_byte:
            file.read_file()
        else:
            file.read_bytes(4)  # 00 * 8 half which is probably the below but unsure which

        count3 = file.read_uint_32()
        file.read_bytes(count3 * 2)
