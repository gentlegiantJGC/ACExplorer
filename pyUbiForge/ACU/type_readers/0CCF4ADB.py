from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '0CCF4ADB'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(4)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(1)

		file_object_data_wrapper.out_file_write('\n')

		for _ in range(7):
			file_object_data_wrapper.read_float_32()
		file_object_data_wrapper.read_bytes(3)
