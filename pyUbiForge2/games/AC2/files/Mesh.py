from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class Mesh(BaseFile):
    ResourceType = 0x415D9568

    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        self.graphic_object = file.read_file_data(0, 0xEC6AC357)

        count1 = file.read_uint_32()
        for _ in range(count1):
            sub_mesh = file.read_file_switch()
            assert sub_mesh.resource_type == 0x5755DE7F, "Expected a SubMesh"

        bone_count = file.read_uint_32()
        for _ in range(bone_count):
            bone = file.read_file()
            assert bone.resource_type == 0x9EF0E7A1, "Expected a MeshBone"

        self.compiled_mesh = file.read_header_file()
        assert self.compiled_mesh.resource_type == 0xFC9E1595, "Expected a CompiledMesh"

        count = file.read_uint_32()
        for _ in range(count):
            switch = file.read_uint_8()
            if switch == 0:
                file.read_uint_8()  # may be unused
                file.read_uint_32()
                file.read_uint_32()
                raise NotImplementedError
                # code
            elif switch == 1:
                file.read_uint_8()
                file.read_uint_32()
            else:
                file.read_uint_8()  # may be unused
                file.read_uint_32()
        file.read_uint_8()
        file.read_uint_8()
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_16()
