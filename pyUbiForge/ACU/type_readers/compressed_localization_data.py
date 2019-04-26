from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'D28389B5'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		block_size = file_object_data_wrapper.read_uint_32()
		self.compressed_block = file_object_data_wrapper.read_bytes(block_size)
