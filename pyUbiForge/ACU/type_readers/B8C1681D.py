from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'B8C1681D'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.read_file()
		count2 = file_object_data_wrapper.read_uint_32()
		for _ in range(count2):
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_id()
		count3 = file_object_data_wrapper.read_uint_32()
		for _ in range(count3):
			file_object_data_wrapper.read_uint_16()


		#01 00 00 00 00 00 00 00 00 00 00 00 00 00
		# 14 bytes