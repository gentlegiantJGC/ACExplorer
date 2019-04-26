from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'AA8F96B6'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(11)
		for _ in range(5):
			file_object_data_wrapper.read_float_32()
		file_object_data_wrapper.read_bytes(10)
		# file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.out_file_write('\n')
