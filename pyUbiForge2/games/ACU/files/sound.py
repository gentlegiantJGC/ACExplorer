from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('83EC6C6D')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        type_id_or_something = file.read_uint_32()
        assert 0 <= file.read_uint_8() <= 1, "check byte should be 0 or 1"
        file_name_size = file.read_uint_32()
        if file_name_size:
            file_name = file.read_bytes(file_name_size)
            assert file.read_uint_8() == 0, "check byte should be 0"
        # assert file.read_uint_8() == 0, "check byte should be 0"

        # more stuff after this
        # file.read_bytes(34)
        # count1 = file.read_uint_32()
        # for _ in range(count1):
        #     file.read_bytes(1)
        #     file.read_file()
