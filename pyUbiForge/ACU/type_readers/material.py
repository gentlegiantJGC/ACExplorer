from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '85C817C3'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(2)
		self.material_set = file_object_data_wrapper.read_id()

		# py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
		# file_object_data_wrapper.read_id()
