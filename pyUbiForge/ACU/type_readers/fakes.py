from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'C69A7F31'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		ent_count = file_object_data_wrapper.read_uint_32()
		for _ in range(ent_count):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
		ent_count2 = file_object_data_wrapper.read_uint_32()
		for _ in range(ent_count2):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
		file_object_data_wrapper.read_bytes(1)
