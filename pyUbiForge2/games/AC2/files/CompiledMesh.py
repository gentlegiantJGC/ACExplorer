from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class CompiledMesh(BaseFile):
    ResourceType = 0xFC9E1595
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        # file.read_file_data(0, 0x85D90806)
        bcount = file.read_uint_32()
        file.read_bytes(bcount)
        self.mesh_data = file.read_file()
        assert self.mesh_data.resource_type == 0x0645ABB5, "Expected a CompiledMesh"
        count = file.read_uint_32()
        for _ in range(count):
            mid = file.read_file()
            assert mid.resource_type == 0xB1D34C1, "Expected a MeshInstancingData"
        file.read_uint_32()
        file.read_uint_32()
