from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'FA58ABDC'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(10, out_file, indent_count)
		file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.read_bytes(23, out_file, indent_count)
		for _ in range(3):
			file_object_data_wrapper.read_bytes(2, out_file, indent_count)
			file_object_data_wrapper.read_id(out_file, indent_count)
