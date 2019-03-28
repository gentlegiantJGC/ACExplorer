from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'DF5D6C0E'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(44, out_file, indent_count)
		for _ in range(3):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
