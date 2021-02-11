import numpy

from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader


@register_file_reader('9EF0E7A1')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        self.bone_id = file.read_resource_type()  # bone name?
        # self.bone_name = pyUbiForge.game_functions.resource_types.get(self.bone_id, self.bone_id)
        self.transformation_matrix = file.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
        file.read_bytes(1)
