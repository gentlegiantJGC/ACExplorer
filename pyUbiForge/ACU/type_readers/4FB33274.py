from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '4FB33274'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		check = file_object_data_wrapper.read_uint_8()
		if check == 1:
			file_object_data_wrapper.read_bytes(3)
