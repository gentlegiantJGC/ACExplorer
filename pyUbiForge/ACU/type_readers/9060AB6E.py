from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '9060AB6E'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(72, out_file, indent_count)
		py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
