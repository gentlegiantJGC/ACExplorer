from pyUbiForge.misc.file_object import FileObjectDataWrapper

file_type = 'AC2BBF68'

class plugin:
	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		self.files = []
		for _ in range(count1):
			file_object_data_wrapper.read_str(2, out_file)
			self.files.append(file_object_data_wrapper.read_id(out_file, indent_count))
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		count2 = file_object_data_wrapper.read_uint_32(out_file, indent_count)  # seems to be about the same or slightly less than count1
		file_object_data_wrapper.read_uint_32(out_file, indent_count)  # this might be a 64 bit int
		file_object_data_wrapper.read_str(4, out_file)
