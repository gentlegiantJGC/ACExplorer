from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class MeshInstancingData(BaseFile):
    ResourceType = 0xB1D34C1
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        file.read_uint_8()
        file.read_uint_8()
        file.read_uint_8()
        file.read_uint_8()
        file.read_uint_16()
        file.read_file_switch()
        for _ in range(0x2A):
            file.read_uint_8()
