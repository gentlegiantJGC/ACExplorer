from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'FBB63E47'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		for _ in range(2):
			file_object_data_wrapper.read_file()

		file_object_data_wrapper.read_bytes(2)
		self.fakes = file_object_data_wrapper.read_id()

		file_object_data_wrapper.read_bytes(2)
		file_object_data_wrapper.read_id()

		# sequence data table
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.read_id()

		file_object_data_wrapper.read_bytes(2)
		file_object_data_wrapper.read_file()
