from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '21795599'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		for length in [2, 2, 1, 1, 4, 2, 2]:
			count = file_object_data_wrapper.read_uint_32(out_file, indent_count)
			file_object_data_wrapper.read_str(count * length, out_file, indent_count + 1)
		count2 = 0
		count3 = 0
		count4 = 0
		# probably not right but this seems to work
		while count2 < count:# or count3 != count4:
			check_byte = file_object_data_wrapper.read_uint_8(out_file, indent_count)
			count4 += 1
			if check_byte == 0:
				sub_file_container = py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
				count2 += sub_file_container.count
				count3 += 2
			elif check_byte == 3:
				continue
			else:
				raise Exception(f'{__name__}: check_byte is not in 0, 3')
		# check_byte = file_object_data_wrapper.read_uint_8(out_file, indent_count)
		# if check_byte != 0:
		# 	raise Exception(f'{__name__}: check_byte is not 0')
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
