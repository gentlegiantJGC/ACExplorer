from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '4FB33274'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		check = file_object_data_wrapper.read_uint_8(out_file, indent_count)
		if check == 1:
			file_object_data_wrapper.read_bytes(3, out_file, indent_count)
