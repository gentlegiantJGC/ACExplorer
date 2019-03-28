from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'AA8F96B6'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(11, out_file, indent_count)
		for _ in range(5):
			file_object_data_wrapper.read_float_32(out_file, indent_count)
		file_object_data_wrapper.read_bytes(10, out_file, indent_count)
		# file_object_data_wrapper.read_bytes(1, out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
