from pyUbiForge2 import BaseFile, FileDataWrapper
from . import register_file_reader


@register_file_reader
class SubMesh(BaseFile):
    ResourceType = 0x5755DE7F
    
    def __init__(
        self,
        file_id: int,
        file: FileDataWrapper
    ):
        super().__init__(file_id, file)
        file.read_uint_32()
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4)
        count = file.read_uint_32()
        for _ in range(count):
            f = file.read_file()
            assert f.resource_type == 0x325C97EE, "Expected a FaceInfo"
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4)
        bcount = file.read_uint_32()
        file.read_bytes(bcount)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4*3)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4*3)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4*3)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4*3)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4*4)
        bcount = file.read_uint_32()
        file.read_bytes(bcount)
        bcount = file.read_uint_32()
        file.read_bytes(bcount*4)
        count = file.read_uint_32()
        for _ in range(count):
            uv = file.read_file()  # FUN_01616d10
            assert uv.resource_type == 0xBDAD8273, "Expected a UVChannel"

        # FUN_014a0640
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
        file.read_file_switch()
