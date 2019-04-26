from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy
import logging


class Reader(BaseReader):
	file_type = '536E963B'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(1)
		self.mesh_id = file_object_data_wrapper.read_id()
		file_object_data_wrapper.read_bytes(40)  # contains a compiled mesh instance 4368101B
		count1 = file_object_data_wrapper.read_uint_32()  # number of textures to follow
		file_object_data_wrapper.out_file_write('\n')
		for n in range(count1):
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_file()

		# file_object_data_wrapper.read_bytes(8) # two counts. first count for transformation matrix. second for more things?
		count2 = file_object_data_wrapper.read_uint_32()
		if count2 > 10000:
			logging.warning('count2:{} is too large. Aborting'.format(count2))
			raise Exception()
		self.transformation_matrix = []
		for _ in range(count2):
			self.transformation_matrix.append(file_object_data_wrapper.read_numpy(numpy.float32, 64).reshape((4, 4), order='F'))
			file_object_data_wrapper.out_file_write('\n')
		count3 = file_object_data_wrapper.read_uint_32()
		if count3 > 10000:
			raise Exception('count3 is too large. Aborting')
		self.bounding_box = []
		for _ in range(count3):
			sub_file_container = file_object_data_wrapper.read_file()
			if sub_file_container.file_type == '4AEC3476':
				self.bounding_box.append(sub_file_container.bounding_box)
		file_object_data_wrapper.out_file_write('\n')
