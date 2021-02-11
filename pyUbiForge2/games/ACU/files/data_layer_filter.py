from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('DB1D406E')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        count1 = file.read_uint_32()  # count
        # more data follows this if count != 0
        for _ in range(count1):
            file.read_file()
        file.out_file_write('\n')
