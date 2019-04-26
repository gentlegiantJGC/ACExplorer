from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'AC2BBF68'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_uint_32()
		self.files = []
		for _ in range(count1):
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(2)
			self.files.append(file_object_data_wrapper.read_id())
			file_object_data_wrapper.indent(-1)
		file_object_data_wrapper.out_file_write('\n')
		count2 = file_object_data_wrapper.read_uint_32()  # seems to be about the same or slightly less than count1
		self.cell_id = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_bytes(4)  # this might be part of the previous as a 64 bit uint
