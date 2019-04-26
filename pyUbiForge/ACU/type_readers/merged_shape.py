from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy
import logging


class Reader(BaseReader):
	file_type = '2D675BA2'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_uint_32()  # possibly a count
		if count1 != 0:
			logging.warning('"2D675BA2" count1 is not 0')
		count2 = file_object_data_wrapper.read_uint_32()
		for _ in range(count2):
			file_object_data_wrapper.read_bytes(2)
			file_object_data_wrapper.read_id()
		file_object_data_wrapper.out_file_write('\n')
		count3 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.out_file_write('\n')
		self.transformation_matrix = []
		for _ in range(count3):  # transformation matrix
			self.transformation_matrix.append(file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F'))
			file_object_data_wrapper.out_file_write('\n')

		count4 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.out_file_write('\n')
		for _ in range(count4):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.out_file_write('\n')
