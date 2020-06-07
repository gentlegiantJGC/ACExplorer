from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('D0C34A81')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(1)
        file.read_file_id()
        file.read_bytes(5)
        count = file.read_uint_32()
        file.read_bytes(1)
        for _ in range(count):
            file.read_file()
        file.read_bytes(16)
