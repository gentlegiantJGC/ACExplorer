from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('502CC335')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(2)
        count = file.read_uint_32()
        for _ in range(count):
            file.read_bytes(2)
            file.read_file()
            # might be part of 7270FC9D
            file.read_bytes(2)
            count = file.read_uint_32()
            for _ in range(count):
                file.read_bytes(2)
                file.read_file()
            file.read_bytes(4)  # E8 03 00 00
            for _ in range(3):
                file.read_bytes(2)
                file.read_file_id()

        count = file.read_uint_32()
        for _ in range(count):
            file.read_bytes(1)
            file.read_file_id()
