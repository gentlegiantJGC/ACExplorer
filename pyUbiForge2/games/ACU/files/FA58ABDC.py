from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('FA58ABDC')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(10)
        file.read_file_id()
        file.read_bytes(23)
        for _ in range(3):
            file.read_bytes(2)
            file.read_file_id()
