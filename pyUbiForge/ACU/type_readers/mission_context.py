from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '414FF9F7'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(1)
		count1 = file_object_data_wrapper.read_uint_32()
		for _ in range(count1):
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.read_id()
			file_object_data_wrapper.read_type()
			file_object_data_wrapper.read_bytes(4)
			file_object_data_wrapper.out_file_write('\n')
		file_object_data_wrapper.out_file_write('\n')
