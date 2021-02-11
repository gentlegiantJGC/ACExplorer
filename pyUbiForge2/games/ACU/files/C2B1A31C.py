from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('C2B1A31C')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(4)
        file.read_float_32()
        file.read_bytes(1)
        count = file.read_uint_32()
        for n in range(count):
            file.read_file()
        file.read_bytes(1)
        file.read_file()
        file.read_bytes(26)
        file.read_file_id()
        file.read_bytes(8)
