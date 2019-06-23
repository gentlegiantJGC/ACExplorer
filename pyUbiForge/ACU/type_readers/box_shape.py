from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '4EC68E98'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_struct('5f')
		file_object_data_wrapper.read_struct('16f')
		file_object_data_wrapper.read_bytes(10)
