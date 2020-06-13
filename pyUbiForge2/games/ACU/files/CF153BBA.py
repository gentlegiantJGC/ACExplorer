from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('CF153BBA')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_bytes(1)
        file.read_file_id()  # same as the top level parent
        assert file.read_uint_32() == 3, "expected 3"
        file.read_numpy("float32", 396)
        file.read_bytes(2)
