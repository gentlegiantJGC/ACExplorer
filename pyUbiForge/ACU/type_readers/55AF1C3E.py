from pyUbiForge.misc.file_object import FileObjectDataWrapper

file_type = '55AF1C3E'

class plugin:
	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(2, out_file)
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		for _ in range(count1):
			file_object_data_wrapper.read_str(41, out_file)
		count2 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		file_object_data_wrapper.read_str(12 * count2, out_file)
		for _ in range(2):
			py_ubi_forge.read_file(file_object_data_wrapper, out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
