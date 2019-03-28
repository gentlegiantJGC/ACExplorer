from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'AC2BBF68'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		self.files = []
		for _ in range(count1):
			file_object_data_wrapper.read_bytes(2, out_file, indent_count + 1)
			self.files.append(file_object_data_wrapper.read_id(out_file, indent_count+1))
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		count2 = file_object_data_wrapper.read_uint_32(out_file, indent_count)  # seems to be about the same or slightly less than count1
		self.cell_id = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		file_object_data_wrapper.read_bytes(4, out_file, indent_count)  # this might be part of the previous as a 64 bit uint
