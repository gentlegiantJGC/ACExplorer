from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy
import logging


class Reader(BaseReader):
	file_type = '3F742D26'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		check_byte = file_object_data_wrapper.read_uint_8()  # checkbyte 03 to continue (other stuff to not? have seen 00 with data after)
		if check_byte == 0:
			for _ in range(2):
				file_object_data_wrapper.read_file()
		file_object_data_wrapper.out_file_write('Transformation Matrix\n')
		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')

		file_object_data_wrapper.out_file_write('\n')
		count1 = file_object_data_wrapper.read_uint_32()
		if count1 > 10000:
			logging.warning('error reading entity file')
			# convert to an actual logger
			raise Exception

		self.nested_files = []

		for _ in range(count1):
			file_object_data_wrapper.out_file_write('\n')
			file_object_data_wrapper.indent()
			if file_object_data_wrapper.read_bytes(2) not in [b'\x04\x00', b'\x00\x01']:  # 04 00
				raise Exception
			file_object_data_wrapper.indent(-1)

			self.nested_files.append(file_object_data_wrapper.read_file())

		file_object_data_wrapper.out_file_write('\n')

		file_object_data_wrapper.read_bytes(43)

		# data layer filter
		# 4 count, more data in here sometimes
		for _ in range(3):
			file_object_data_wrapper.read_file()

		# 03 end file?
		check_byte_2 = file_object_data_wrapper.read_uint_8()
		if check_byte_2 == 0:
			file_object_data_wrapper.read_file()
		elif check_byte_2 != 3:
			raise Exception
		file_object_data_wrapper.out_file_write('\n')
