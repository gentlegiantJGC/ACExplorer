from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'B0438131'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_bytes(count1)
