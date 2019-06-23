from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '939B245D'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(22)
		file_object_data_wrapper.read_file()    # gameplay surface nav type
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(22)
		file_object_data_wrapper.read_float_32()
		file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(39)
