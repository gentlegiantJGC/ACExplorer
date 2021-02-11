from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import numpy
import logging


@register_file_reader('2D675BA2')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):

        BaseFile.__init__(self, file_id)
        count1 = file.read_uint_32()  # possibly a count
        if count1 != 0:
            logging.warning('"2D675BA2" count1 is not 0')
        count2 = file.read_uint_32()
        for _ in range(count2):
            file.read_bytes(2)
            file.read_file_id()
        file.out_file_write('\n')
        count3 = file.read_uint_32()
        file.out_file_write('\n')
        self.transformation_matrix = []
        for _ in range(count3):  # transformation matrix
            self.transformation_matrix.append(file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F'))
            file.out_file_write('\n')

        count4 = file.read_uint_32()
        file.out_file_write('\n')
        for _ in range(count4):
            file.read_file()
        file.out_file_write('\n')
