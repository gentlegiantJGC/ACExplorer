from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('FBB63E47')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        for _ in range(2):
            file.read_file()

        file.read_bytes(2)
        self.fakes = file.read_file_id()

        file.read_bytes(2)
        file.read_file_id()

        # sequence data table
        count = file.read_uint_32()
        for _ in range(count):
            file.read_bytes(2)
            file.read_file_id()

        file.read_bytes(2)
        file.read_file()
