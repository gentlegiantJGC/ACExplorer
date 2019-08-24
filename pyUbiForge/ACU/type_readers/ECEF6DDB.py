from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'ECEF6DDB'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count2 = file_object_data_wrapper.read_uint_32()
		for _ in range(count2):
			file_object_data_wrapper.read_file()
