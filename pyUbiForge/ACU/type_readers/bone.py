from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '9EF0E7A1'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(4, out_file, indent_count)  # bone name?
		file_object_data_wrapper.read_numpy(numpy.float32, 64, out_file, indent_count).reshape((4, 4), order='F')
		file_object_data_wrapper.read_bytes(1, out_file, indent_count)
