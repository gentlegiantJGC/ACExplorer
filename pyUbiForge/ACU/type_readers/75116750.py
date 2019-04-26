from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '75116750'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(5)
		count = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_bytes(1)
		for _ in range(count):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_file()
			file_object_data_wrapper.indent(-1)
		file_object_data_wrapper.read_bytes(16)
