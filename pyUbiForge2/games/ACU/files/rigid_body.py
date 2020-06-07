from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import numpy


@register_file_reader('228F402A')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            resource_type: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id, resource_type)
        file.read_file()
        file.read_file_id()
        file.read_bytes(2)
        file.read_bytes(17)
        file.out_file_write('Transformation Matrix\n')
        self.transformation_matrix = file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
