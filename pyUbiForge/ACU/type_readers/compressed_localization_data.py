from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'D28389B5'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		block_size = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		self.compressed_block = file_object_data_wrapper.read_str(block_size, out_file, indent_count)
