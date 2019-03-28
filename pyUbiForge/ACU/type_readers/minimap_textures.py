from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'EE568905'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		self.width = self.height = int(count1**0.5)
		self.image_ids = []
		for n in range(count1):
			file_object_data_wrapper.read_bytes(1, out_file, indent_count + 1)
			self.image_ids.append(file_object_data_wrapper.read_id(out_file, indent_count + 1))
