from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '7F57D331'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(16, out_file, indent_count)
		something = file_object_data_wrapper.read_bytes(4, out_file, indent_count)
		while something != b'\x14\x10\x67\x4C':
			file_object_data_wrapper.read_bytes(16, out_file, indent_count)
			something = file_object_data_wrapper.read_bytes(4, out_file, indent_count)
		file_object_data_wrapper.read_bytes(49, out_file, indent_count)
