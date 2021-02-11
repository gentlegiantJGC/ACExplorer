from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('BC300CF6')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(2)
        count = file.read_uint_32()
        for _ in range(count):
            file.read_bytes(2)
            file.read_file()
        file.read_struct('8f')
        file.read_bytes(1)
