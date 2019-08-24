from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '95741049'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		self.bone_id = file_object_data_wrapper.read_type()

		self.parent = None

		if file_object_data_wrapper.read_uint_8() != 3:
			self.parent = file_object_data_wrapper.read_id()

		if file_object_data_wrapper.read_uint_8() != 3:
			file_object_data_wrapper.read_id()  # perhaps child id

		file_object_data_wrapper.read_bytes(64)  # trm mtx?

		file_object_data_wrapper.read_bytes(5)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_file()
			file_object_data_wrapper.indent(-1)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_type()
			file_object_data_wrapper.indent(-1)
		# check = file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_bytes(13)
