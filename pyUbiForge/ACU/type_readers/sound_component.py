from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'E8134060'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		for _ in range(3):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(10)  # wrong but needs more examples
