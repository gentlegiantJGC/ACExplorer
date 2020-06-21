from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('24AECB7C')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(4)
        count = file.read_uint_32()
        self.bones = []
        for _ in range(count):
            assert file.read_uint_8() == 0, "Check byte failed"
            self.bones.append(
                file.read_file()
            )

        if file.read_uint_8() == 2:
            file.read_bytes(66)
            if file.read_uint_8() != 3:
                assert file.read_uint_8() == 0, "Check byte failed"
                file.read_file()
            file.read_bytes(8)
