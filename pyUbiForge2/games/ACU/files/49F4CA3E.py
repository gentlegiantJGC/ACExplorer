from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('49F4CA3E')
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
        for _ in range(2):
            check_byte = file.read_uint_8()
            if check_byte != 3:
                file.read_file_id()

        file.read_bytes(32)
