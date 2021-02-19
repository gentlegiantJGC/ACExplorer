from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class FaceInfo(BaseFile):
    ResourceType = 0x325C97EE
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        file.read_uint_32()
        file.read_uint_8()
        file.read_uint_8()
        file.read_uint_8()
