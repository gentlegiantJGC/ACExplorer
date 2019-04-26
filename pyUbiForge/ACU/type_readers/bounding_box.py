from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '4AEC3476'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		self.bounding_box = file_object_data_wrapper.read_numpy(numpy.float32, 24).reshape((3, 2))
		file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.out_file_write('\n')
