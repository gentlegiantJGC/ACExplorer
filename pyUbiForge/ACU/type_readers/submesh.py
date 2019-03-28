from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '5755DE7F'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_uint_32(out_file, indent_count)  # should always be equal to 0
		for n in (4, 4, 4, 1, 12, 12, 12, 12, 4, 4):
			count = file_object_data_wrapper.read_uint_32(out_file, indent_count)
			file_object_data_wrapper.read_bytes(count * n, out_file, indent_count + 1)
		file_object_data_wrapper.read_bytes(1, out_file, indent_count)
		for n in (4, 2, 2):
			count = file_object_data_wrapper.read_uint_32(out_file, indent_count)
			file_object_data_wrapper.read_bytes(count * n, out_file, indent_count + 1)

		for _ in range(file_object_data_wrapper.read_uint_32(out_file, indent_count)):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)

		file_object_data_wrapper.read_bytes(2, out_file, indent_count)
		file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.read_bytes(1, out_file, indent_count)
