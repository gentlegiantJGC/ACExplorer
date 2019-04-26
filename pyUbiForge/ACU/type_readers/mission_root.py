from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'E6545731'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_int_32()
		for _ in range(count1):
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.read_id()
		file_object_data_wrapper.out_file_write('\n')
		count2 = file_object_data_wrapper.read_int_32()
		for _ in range(count2):
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.read_file()
