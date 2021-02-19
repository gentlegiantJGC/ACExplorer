from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class UVChannel(BaseFile):
    ResourceType = 0xBDAD8273
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        file.read_uint_32()
        file.read_uint_8()
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4*2)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4*1)
