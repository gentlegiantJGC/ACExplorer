from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('43F19E3B')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        header = file.read_bytes(21)  # all 00
        count = file.read_uint_8()
        for _ in range(count):
            file.read_bytes(5)
            file.read_file()
        assert all(b == 0 for b in header), "expected header to be all 00"
