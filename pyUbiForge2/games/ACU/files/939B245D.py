from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('939B245D')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(22)
        file.read_file()  # gameplay surface nav type
        count = file.read_uint_32()
        for _ in range(count):
            file.read_file()
        file.read_bytes(22)
        file.read_float_32()
        file.read_file()
        file.read_bytes(39)
