from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '24AECB7C'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(4)
		count = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_bytes(1)
		for _ in range(count):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
