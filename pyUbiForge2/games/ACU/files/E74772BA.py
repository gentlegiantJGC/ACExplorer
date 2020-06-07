from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('E74772BA')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):

        BaseFile.__init__(self, file_id, resource_type)
        file.read_uint_32()
        file.read_uint_32()
