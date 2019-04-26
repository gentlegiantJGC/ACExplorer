from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'D3F7FFC8'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(4)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.indent(-1)
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(4)
