from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '21795599'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		for length in [2, 2, 1, 1, 4, 2, 2]:
			total_count = file_object_data_wrapper.read_uint_32()
			file_object_data_wrapper.indent()
			file_object_data_wrapper.read_bytes(total_count * length)
			file_object_data_wrapper.indent(-1)
		found_count = 0
		empty_count = 0
		filled_count = 0
		# probably not right but this seems to work
		while found_count < total_count or empty_count != filled_count + 1:
			check_byte = file_object_data_wrapper.read_uint_8()
			if check_byte == 0:
				sub_file_container = file_object_data_wrapper.read_file()
				found_count += sub_file_container.count
				if sub_file_container.count > 0:
					filled_count += 1
				else:
					empty_count += 1

			elif check_byte == 3:
				filled_count += 1
				continue
			else:
				raise Exception(f'{__name__}: check_byte is not in 0, 3')
		file_object_data_wrapper.read_bytes(8)
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			check_byte = file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_file()
		count = file_object_data_wrapper.read_uint_32()
		for _ in range(count):
			file_object_data_wrapper.read_bytes(4)
		file_object_data_wrapper.read_bytes(1)
		for _ in range(7):
			file_object_data_wrapper.read_bytes(4)
		file_object_data_wrapper.read_file()
