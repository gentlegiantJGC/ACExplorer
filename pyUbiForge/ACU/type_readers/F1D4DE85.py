from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'F1D4DE85'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(44)
		count = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_struct(f'{count*4}f')
