from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '509C4552'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(8)
		file_object_data_wrapper.read_bytes(4 * 4)  # 4 floats
		file_object_data_wrapper.read_bytes(4)
		file_object_data_wrapper.out_file_write('\n')
