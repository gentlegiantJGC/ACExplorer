from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '7313743E'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_bytes(10)
		for _ in range(count1):
			file_object_data_wrapper.read_file()
