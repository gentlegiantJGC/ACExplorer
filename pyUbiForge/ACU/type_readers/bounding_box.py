from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '4AEC3476'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		self.bounding_box = file_object_data_wrapper.read_numpy(numpy.float32, 24, out_file, indent_count).reshape((3, 2))
		file_object_data_wrapper.read_uint_32(out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
