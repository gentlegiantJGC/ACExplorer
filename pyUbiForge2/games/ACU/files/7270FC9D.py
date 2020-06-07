from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('7270FC9D')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        for _ in range(2):
            count1 = file.read_uint_32()
            for _ in range(count1):
                file.read_bytes(1)
                file.read_file_id()
