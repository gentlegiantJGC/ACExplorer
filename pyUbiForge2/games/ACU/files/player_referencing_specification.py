from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('9E1CD34A')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        count = file.read_uint_32()
        # for _ in range(count):  # the above looks like a count but there is only 1 of the below
        file.read_file()
