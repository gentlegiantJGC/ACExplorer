from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '21795599'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		for length in [2, 2, 1, 1, 4, 2, 2]:
			total_count = file_object_data_wrapper.read_uint_32(out_file, indent_count)
			file_object_data_wrapper.read_str(total_count * length, out_file, indent_count + 1)
		found_count = 0
		empty_count = 0
		filled_count = 0
		# probably not right but this seems to work
		while found_count < total_count or empty_count != filled_count + 1:
			check_byte = file_object_data_wrapper.read_uint_8(out_file, indent_count)
			if check_byte == 0:
				sub_file_container = py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
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
		file_object_data_wrapper.read_str(8, out_file, indent_count)
		count = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		for _ in range(count):
			check_byte = file_object_data_wrapper.read_str(1, out_file, indent_count)
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		count = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		for _ in range(count):
			file_object_data_wrapper.read_str(4, out_file, indent_count)
		file_object_data_wrapper.read_str(1, out_file, indent_count)
		for _ in range(7):
			file_object_data_wrapper.read_str(4, out_file, indent_count)
		py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
