from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'BDAD8273'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(5, out_file, indent_count)
		for n in (8, 4):
			count = file_object_data_wrapper.read_uint_32(out_file, indent_count)
			file_object_data_wrapper.read_str(count * n, out_file, indent_count+1)
