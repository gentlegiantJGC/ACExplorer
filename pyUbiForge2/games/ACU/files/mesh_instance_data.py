from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
import numpy
import logging


@register_file_reader('536E963B')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        file.read_bytes(1)
        self.mesh_id = file.read_file_id()
        file.read_bytes(40)  # contains a compiled mesh instance 4368101B
        count1 = file.read_uint_32()  # number of textures to follow
        file.out_file_write('\n')
        for n in range(count1):
            file.read_bytes(1)
            file.read_file()

        # file.read_bytes(8) # two counts. first count for transformation matrix. second for more things?
        count2 = file.read_uint_32()
        if count2 > 10000:
            logging.warning('count2:{} is too large. Aborting'.format(count2))
            raise Exception()
        self.transformation_matrix = []
        for _ in range(count2):
            self.transformation_matrix.append(file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F'))
            file.out_file_write('\n')
        count3 = file.read_uint_32()
        if count3 > 10000:
            raise Exception('count3 is too large. Aborting')
        self.bounding_box = []
        for _ in range(count3):
            sub_file_container = file.read_file()
            if sub_file_container.resource_type == '4AEC3476':
                self.bounding_box.append(sub_file_container.bounding_box)
        file.out_file_write('\n')
