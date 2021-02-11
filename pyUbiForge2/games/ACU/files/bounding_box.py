from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import numpy


@register_file_reader('4AEC3476')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        self.bounding_box = file.read_numpy(numpy.float32, 24).reshape((3, 2))
        file.read_uint_32()
        file.out_file_write('\n')
