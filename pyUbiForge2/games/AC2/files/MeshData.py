from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class MeshData(BaseFile):
    ResourceType = 0x0645ABB5
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        file.read_uint_8()
        file.read_uint_8()
        file.read_uint_8()
        for _ in range(2):
            count = file.read_uint_32()
            for _ in range(count):
                mesh_primitive = file.read_file()
                assert mesh_primitive.resource_type == 0xA57387EF, "Expected a MeshPrimitive"
        for _ in range(6):
            bcount = file.read_uint_32()
            file.read_bytes(bcount)
