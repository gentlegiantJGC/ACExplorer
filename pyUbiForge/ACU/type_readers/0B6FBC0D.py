from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '0B6FBC0D'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(8)
		for _ in range(8):
			file_object_data_wrapper.read_float_32()
		file_object_data_wrapper.read_bytes(16)
