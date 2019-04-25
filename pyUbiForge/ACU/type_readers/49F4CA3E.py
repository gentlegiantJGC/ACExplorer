from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '49F4CA3E'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(5)
		for _ in range(2):
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_id()

		file_object_data_wrapper.read_bytes(32)
