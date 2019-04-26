from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '85C817C3'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(2)
		self.material_set = file_object_data_wrapper.read_id()

		# file_object_data_wrapper.read_file()
		# file_object_data_wrapper.read_id()
