from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import numpy


@register_file_reader('1CBDE084')
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
        file.out_file_write('\n')

        for _ in range(2):
            file.read_file()

        self.transformation_matrix = file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
        file.out_file_write('\n')

        count1 = file.read_uint_32()

        self.files = []

        for _ in range(count1):
            file.read_bytes(1)
            self.files.append(
                file.read_file_id()
            )
        file.out_file_write('\n')
