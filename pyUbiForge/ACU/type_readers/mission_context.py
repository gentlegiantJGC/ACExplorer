from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '414FF9F7'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(1, out_file, indent_count)
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		for _ in range(count1):
			file_object_data_wrapper.read_str(2, out_file, indent_count)
			file_object_data_wrapper.read_id(out_file, indent_count)
			file_object_data_wrapper.read_type(out_file, indent_count)
			file_object_data_wrapper.read_str(4, out_file, indent_count)
			file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
