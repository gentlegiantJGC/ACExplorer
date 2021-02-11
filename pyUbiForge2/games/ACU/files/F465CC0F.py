from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('F465CC0F')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):

        BaseFile.__init__(self, file_id)
        file.read_bytes(1)
        file.read_file_id()
        file.read_bytes(5)
        count = file.read_uint_32()  # zero
        file.read_bytes(1)
        file.read_file_id()
        file.read_bytes(17)
        count2 = file.read_uint_32()
        for _ in range(count2):
            file.indent()
            file.read_bytes(1)
            file.read_file()
            file.indent(-1)
