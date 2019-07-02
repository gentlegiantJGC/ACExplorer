from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '0E5A450A'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		# readStr(fIn, fOut, 184)
		file_object_data_wrapper.read_bytes(14)
		for _ in range(2):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(1)
		check_byte = file_object_data_wrapper.read_uint_8()
		if check_byte != 3:
			file_object_data_wrapper.read_id()
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(9)
