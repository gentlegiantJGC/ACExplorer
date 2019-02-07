from pyUbiForge.misc.file_object import FileObjectDataWrapper

file_type = '43EF99C2'

class plugin:
	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(15, out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
