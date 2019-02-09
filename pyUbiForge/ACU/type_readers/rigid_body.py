from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '228F402A'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(29, out_file, indent_count)
		file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.read_str(17, out_file, indent_count)
		file_object_data_wrapper.out_file_write('Transformation Matrix\n', out_file, indent_count)
		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64, out_file, indent_count).reshape((4, 4))
