from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '5755DE7F'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_uint_32()  # should always be equal to 0
		for n in (4, 4, 4, 1, 12, 12, 12, 12, 4, 4):
			count = file_object_data_wrapper.read_uint_32()
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(count * n)
			file_object_data_wrapper.indent(-1)
		file_object_data_wrapper.read_bytes(1)
		for n in (4, 2, 2):
			count = file_object_data_wrapper.read_uint_32()
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(count * n)
			file_object_data_wrapper.indent(-1)

		for _ in range(file_object_data_wrapper.read_uint_32()):
			file_object_data_wrapper.read_file()

		file_object_data_wrapper.read_bytes(2)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(1)
