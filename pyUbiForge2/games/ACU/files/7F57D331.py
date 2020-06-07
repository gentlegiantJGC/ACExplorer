from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('7F57D331')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(16)
        something = file.read_bytes(4)
        while something != b'\x14\x10\x67\x4C':
            file.read_bytes(16)
            something = file.read_bytes(4)
        file.read_bytes(49)
