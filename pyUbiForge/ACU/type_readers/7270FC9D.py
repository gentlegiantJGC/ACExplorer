from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '7270FC9D'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		for _ in range(2):
			count1 = file_object_data_wrapper.read_uint_32()
			for _ in range(count1):
				file_object_data_wrapper.read_bytes(1)
				file_object_data_wrapper.read_id()
