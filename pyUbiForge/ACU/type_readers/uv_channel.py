from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'BDAD8273'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(5)
		for n in (8, 4):
			count = file_object_data_wrapper.read_uint_32()
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(count * n)
			file_object_data_wrapper.indent(-1)
