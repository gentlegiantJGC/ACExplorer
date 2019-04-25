from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '9EF0E7A1'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		file_id = file_object_data_wrapper.read_type()  # bone name?
		self.bone_id = py_ubi_forge.game_functions.file_types.get(file_id, file_id)
		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
		file_object_data_wrapper.read_bytes(1)
