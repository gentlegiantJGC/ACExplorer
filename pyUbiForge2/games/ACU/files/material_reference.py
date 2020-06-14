from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('995BFBF5')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(1)
        file.read_file_id()
        file.read_bytes(1)
        file.read_file_id()
        file.read_bytes(2)
        file.read_file_id()
        file.out_file_write('\n')