from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '0E2F4444'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_uint_32()
		count2 = file_object_data_wrapper.read_uint_32()

		for _ in range(count2):
			file_object_data_wrapper.read_file()
