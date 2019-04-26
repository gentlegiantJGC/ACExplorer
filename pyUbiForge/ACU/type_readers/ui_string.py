from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '81A7045D'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(9)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(17)
		for _ in range(18):
			file_object_data_wrapper.read_file()
