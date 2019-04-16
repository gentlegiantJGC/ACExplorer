from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '89288371'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		for _ in range(2):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
