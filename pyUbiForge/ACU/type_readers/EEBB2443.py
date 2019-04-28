from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = 'EEBB2443'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		file_object_data_wrapper.read_id()

		for _ in range(3):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_numpy(numpy.float32, 16)
		file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')

		file_object_data_wrapper.read_file()
		file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F')
