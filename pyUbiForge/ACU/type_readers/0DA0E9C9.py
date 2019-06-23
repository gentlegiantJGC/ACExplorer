from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '0DA0E9C9'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(66)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(33)  # 01 followed by 8 floats

