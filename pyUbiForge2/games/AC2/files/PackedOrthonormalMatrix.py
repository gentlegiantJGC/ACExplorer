from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class PackedOrthonormalMatrix(BaseFile):
    ResourceType = 0x05358B33
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_32()
        file.read_uint_32()
