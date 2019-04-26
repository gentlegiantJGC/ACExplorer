from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '5730D30E'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_file()

		count1 = file_object_data_wrapper.read_uint_32()
		for _ in range(count1):
			file_object_data_wrapper.read_bytes(12)

		count2 = file_object_data_wrapper.read_uint_32()
		if count2 != 0:
			raise Exception()
