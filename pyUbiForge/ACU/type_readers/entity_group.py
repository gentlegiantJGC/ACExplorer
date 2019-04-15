from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '3F742D26'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		check_byte = file_object_data_wrapper.read_uint_8(out_file, indent_count)  # checkbyte 03 to continue (other stuff to not? have seen 00 with data after)
		if check_byte == 0:
			for _ in range(2):
				py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		file_object_data_wrapper.out_file_write('Transformation Matrix\n', out_file, indent_count)
		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64, out_file, indent_count).reshape((4, 4), order='F')

		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		if count1 > 10000:
			py_ubi_forge.log.warn(__name__, 'error reading entity file')
			# convert to an actual logger
			raise Exception

		self.nested_files = []

		for _ in range(count1):
			file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
			if file_object_data_wrapper.read_bytes(2, out_file, indent_count + 1) not in [b'\x04\x00', b'\x00\x01']:  # 04 00
				raise Exception

			self.nested_files.append(py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count + 1))

		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)

		file_object_data_wrapper.read_bytes(43, out_file, indent_count)

		# data layer filter
		# 4 count, more data in here sometimes
		for _ in range(3):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)

		# 03 end file?
		check_byte_2 = file_object_data_wrapper.read_uint_8(out_file, indent_count)
		if check_byte_2 == 0:
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		elif check_byte_2 != 3:
			raise Exception
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
