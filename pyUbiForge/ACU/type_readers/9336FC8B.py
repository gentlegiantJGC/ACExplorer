from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '9336FC8B'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(8 * 4, out_file, indent_count)  # FFF0FFF0
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		self.count = count1
		if count1 == 0:
			pass
		elif 0 < count1 < 100000:
			file_object_data_wrapper.read_bytes(count1 * 4, out_file, indent_count + 1)
		else:
			raise Exception('Probably an issue here')
		count2 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		if count2 == 0:
			pass
		elif 0 < count2 < 100000:
			file_object_data_wrapper.read_bytes(count2, out_file, indent_count + 1)
			file_object_data_wrapper.read_bytes(2, out_file, indent_count)    # \x03\x03
		else:
			raise Exception('Probably an issue here')
