from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '4661AAEF'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(2, out_file)
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		file_object_data_wrapper.read_str(2 * count1, out_file, indent_count)
		file_object_data_wrapper.read_str(4 * 6, out_file, indent_count) # 6 floats
		count2 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		for _ in range(count2):
			file_object_data_wrapper.read_str(24, out_file, indent_count)
		file_object_data_wrapper.read_str(1, out_file)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
