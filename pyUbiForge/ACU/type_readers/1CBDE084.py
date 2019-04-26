from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '1CBDE084'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.out_file_write('\n')

		for _ in range(2):
			file_object_data_wrapper.read_file()

		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
		file_object_data_wrapper.out_file_write('\n')

		count1 = file_object_data_wrapper.read_uint_32()

		self.files = []

		for _ in range(count1):
			file_object_data_wrapper.read_bytes(1)
			self.files.append(
				file_object_data_wrapper.read_id()
			)
		file_object_data_wrapper.out_file_write('\n')
