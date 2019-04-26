from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '4E7C39C3'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		for _ in range(2):
			file_object_data_wrapper.read_file()
