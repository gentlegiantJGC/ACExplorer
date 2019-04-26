from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '132FE22D'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		# needs more work
		file_object_data_wrapper.read_bytes(3)
		file_object_data_wrapper.read_id()
		count1 = file_object_data_wrapper.read_uint_32()
		for _ in range(count1 + 1):
			file_object_data_wrapper.read_bytes(1)  # may contain a count
			file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(4 * 9)
		file_object_data_wrapper.out_file_write('\n')
