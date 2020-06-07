from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('5755DE7F')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_uint_32()  # should always be equal to 0
        for n in (4, 4, 4, 1, 12, 12, 12, 12, 4, 4):
            count = file.read_uint_32()
            with file.indent:
                file.read_bytes(count * n)

        file.read_bytes(1)
        for n in (4, 2, 2):
            count = file.read_uint_32()
            with file.indent:
                file.read_bytes(count * n)

        for _ in range(file.read_uint_32()):
            file.read_file()

        file.read_bytes(2)
        file.read_file_id()
        file.read_bytes(1)
