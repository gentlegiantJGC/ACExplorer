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
        self.bone_id = file.read_type()

        self.parent = None

        if file.read_uint_8() != 3:
            self.parent = file.read_file_id()

        if file.read_uint_8() != 3:
            file.read_file_id()  # perhaps child id

        file.read_bytes(64)  # trm mtx?

        file.read_bytes(5)
        count = file.read_uint_32()
        for _ in range(count):
            file.indent()
            file.read_bytes(1)
            file.read_file()
            file.indent(-1)
        count = file.read_uint_32()
        for _ in range(count):
            file.indent()
            file.read_type()
            file.indent(-1)
        # check = file.read_bytes(1)
        file.read_bytes(13)
