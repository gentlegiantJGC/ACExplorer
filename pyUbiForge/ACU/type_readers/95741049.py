from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '95741049'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_type()
		for _ in range(2):
			check = file_object_data_wrapper.read_bytes(1)
			if check != b'\x03':
				file_object_data_wrapper.read_id()
		for _ in range(2):
			file_object_data_wrapper.read_bytes(32)  # ?

		file_object_data_wrapper.read_bytes(5)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(1)
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
			file_object_data_wrapper.indent(-1)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_type()
			file_object_data_wrapper.indent(-1)
		# check = file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_bytes(13)
