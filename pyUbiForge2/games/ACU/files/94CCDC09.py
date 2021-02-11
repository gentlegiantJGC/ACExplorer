from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('94CCDC09')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(33)
        for _ in range(file.read_uint_32()):
            assert file.read_uint_8() == 0, "check byte failed"
            file.read_file_id()

        for _ in range(file.read_uint_32()):
            str_len = file.read_uint_32()
            name = file.read_bytes(str_len)
            assert file.read_uint_8() == 0, "check byte failed"
