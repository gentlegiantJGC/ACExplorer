from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'E6545731'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		count1 = file_object_data_wrapper.read_int_32(out_file, indent_count)
		for _ in range(count1):
			file_object_data_wrapper.read_str(2, out_file, indent_count)
			file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		count2 = file_object_data_wrapper.read_int_32(out_file, indent_count)
		for _ in range(count2):
			file_object_data_wrapper.read_str(2, out_file, indent_count)
			py_ubi_forge.read_file(file_object_data_wrapper, out_file, indent_count)
