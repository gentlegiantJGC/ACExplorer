from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('81A7045D')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):

        BaseFile.__init__(self, file_id)
        file.read_bytes(9)
        file.read_file_id()
        file.read_bytes(17)
        for _ in range(18):
            file.read_file()
