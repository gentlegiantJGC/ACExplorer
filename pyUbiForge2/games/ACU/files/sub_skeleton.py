from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('95741049')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        self.bone_id = file.read_resource_type()

        self.parent = None

        if file.read_uint_8() != 3:
            self.parent = file.read_file_id()

        if file.read_uint_8() != 3:
            file.read_file_id()  # reflected file id. The 

        transform = file.read_numpy("float32", 16*4)

        file.read_bytes(5)
        count = file.read_uint_32()
        for _ in range(count):
            with file.indent:
                file.read_bytes(1)
                file.read_file()
        count = file.read_uint_32()
        for _ in range(count):
            with file.indent:
                file.read_resource_type()
        assert file.read_uint_32() == 7, "this should be 7"
        assert file.read_float_32() == 1, "this should be 1"  # scale factor?
        file.read_uint_16()
        file.read_uint_16()
        file.read_uint_8()  # this may be in the parent file 24AECB7C. Usually 0 but 2 at the end sometimes
