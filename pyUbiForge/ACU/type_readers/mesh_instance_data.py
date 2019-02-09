from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '536E963B'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(1, out_file, indent_count)
		self.mesh_id = file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.read_str(40, out_file, indent_count)  # contains a compiled mesh instance 4368101B
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)  # number of textures to follow
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		for n in range(count1):
			file_object_data_wrapper.read_str(1, out_file, indent_count)
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)

		# file_object_data_wrapper.read_str(8, out_file, indent_count) # two counts. first count for transformation matrix. second for more things?
		count2 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		if count2 > 10000:
			py_ubi_forge.log.warn(__name__, 'count2:{} is too large. Aborting'.format(count2))
			raise Exception()
		self.transformation_matrix = []
		for _ in range(count2):
			self.transformation_matrix.append(file_object_data_wrapper.read_numpy(numpy.float32, 64, out_file, indent_count).reshape((4, 4)))
			file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		count3 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		if count3 > 10000:
			raise Exception('count3 is too large. Aborting')
		self.bounding_box = []
		for _ in range(count3):
			sub_file_container = py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
			if sub_file_container.file_type == '4AEC3476':
				self.bounding_box.append(sub_file_container.bounding_box)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
