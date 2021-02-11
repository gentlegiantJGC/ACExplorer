from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
from pyUbiForge2.games.ACU.files.entity import Reader as Entity


@register_file_reader('D77FB524')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(2)
        self.entity: Entity = file.read_file()
        count1 = file.read_uint_32()
        file.indent()
        for _ in range(count1):
            file.read_file()
        file.indent(-1)
        count2 = file.read_uint_32()
        file.indent()
        file.read_bytes(4 * count2)
        file.indent(-1)
        file.read_uint_32()  # coord 1
        file.read_uint_32()  # coord 2
        file.read_bytes(1)
