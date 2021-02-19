from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class MeshBone(BaseFile):
    ResourceType = 0x9EF0E7A1
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        mat = file.read_file()
        assert mat.resource_type == 0x05358B33, "Expected a PackedOrthonormalMatrix"
        file.read_uint_32()
