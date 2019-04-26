from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '7F57D331'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(16)
		something = file_object_data_wrapper.read_bytes(4)
		while something != b'\x14\x10\x67\x4C':
			file_object_data_wrapper.read_bytes(16)
			something = file_object_data_wrapper.read_bytes(4)
		file_object_data_wrapper.read_bytes(49)
