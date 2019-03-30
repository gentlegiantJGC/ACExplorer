from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'EC658D29'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(4, out_file, indent_count)
		file_object_data_wrapper.read_id(out_file, indent_count)

		file_object_data_wrapper.read_bytes(1, out_file, indent_count)

		self.nested_files = {}

		nested_file = py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		self.nested_files[nested_file.file_type] = nested_file

		file_object_data_wrapper.read_bytes(1, out_file, indent_count)

		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)

		for _ in range(7):
			file_object_data_wrapper.read_float_32(out_file, indent_count)
