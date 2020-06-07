from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('AA8F96B6')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(11)
        for _ in range(5):
            file.read_float_32()
        file.read_bytes(10)
        # file.read_bytes(1)
        file.out_file_write('\n')
