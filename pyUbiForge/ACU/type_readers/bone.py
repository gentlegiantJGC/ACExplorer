from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy
import pyUbiForge


class Reader(BaseReader):
	file_type = '9EF0E7A1'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		self.bone_id = file_object_data_wrapper.read_type()  # bone name?
		# self.bone_name = pyUbiForge.game_functions.file_types.get(self.bone_id, self.bone_id)
		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
		file_object_data_wrapper.read_bytes(1)
