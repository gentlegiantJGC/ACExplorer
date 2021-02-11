from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('0E5A450A')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        # readStr(fIn, fOut, 184)
        file.read_bytes(14)
        for _ in range(2):
            file.read_file()
        file.read_bytes(1)
        check_byte = file.read_uint_8()
        if check_byte != 3:
            file.read_file_id()
        count = file.read_uint_32()
        for _ in range(count):
            file.read_bytes(1)
            file.read_file_id()
        file.read_bytes(9)
