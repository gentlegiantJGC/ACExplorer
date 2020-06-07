from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('85C817C3')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(2)
        file.read_file_id()
        file.read_bytes(2)
        self.material_set = file.read_file_id()
    
    # file.read_file()
    # file.read_file_id()
