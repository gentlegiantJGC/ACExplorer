from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '788BAA0D'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		for _ in range(4):
			for _ in range(4):
				file_object_data_wrapper.read_float_32(out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
