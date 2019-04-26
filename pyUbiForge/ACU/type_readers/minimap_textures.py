from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'EE568905'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_uint_32()
		self.width = self.height = int(count1**0.5)
		self.image_ids = []
		for n in range(count1):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(1)
			self.image_ids.append(file_object_data_wrapper.read_id())
			file_object_data_wrapper.indent(-1)
