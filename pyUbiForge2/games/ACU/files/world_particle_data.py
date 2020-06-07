from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('5730D30E')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):

        BaseFile.__init__(self, file_id, resource_type)
        file.read_file()

        count1 = file.read_uint_32()
        for _ in range(count1):
            file.read_bytes(12)

        count2 = file.read_uint_32()
        if count2 != 0:
            raise Exception()
