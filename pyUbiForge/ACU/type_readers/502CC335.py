from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '502CC335'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.read_file()
			# might be part of 7270FC9D
			file_object_data_wrapper.read_bytes(2)
			count = file_object_data_wrapper.read_uint_32()
			for _ in range(count):
				file_object_data_wrapper.read_bytes(2)
				file_object_data_wrapper.read_file()
			file_object_data_wrapper.read_bytes(4) # E8 03 00 00
			for _ in range(3):
				file_object_data_wrapper.read_bytes(2)
				file_object_data_wrapper.read_id()

		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_id()
