from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'FFA6D96A'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
