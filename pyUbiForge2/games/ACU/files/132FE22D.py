from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('132FE22D')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        # needs more work
        file.read_bytes(3)
        file.read_file_id()
        count1 = file.read_uint_32()
        for _ in range(count1 + 1):
            file.read_bytes(1)  # may contain a count
            file.read_file_id()
        file.read_bytes(4 * 9)
        file.out_file_write('\n')
