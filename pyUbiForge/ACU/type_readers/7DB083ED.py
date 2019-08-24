from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '7DB083ED'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(26)
		check_byte = file_object_data_wrapper.read_uint_8()
		if check_byte:
			file_object_data_wrapper.read_file()
		else:
			file_object_data_wrapper.read_bytes(4)  # 00 * 8 half which is probably the below but unsure which

		count3 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_bytes(count3 * 2)
