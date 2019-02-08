from pyUbiForge.misc.file_object import FileObjectDataWrapper
import numpy

file_type = '2D675BA2'

class plugin:
	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)  # possibly a count
		if count1 != 0:
			py_ubi_forge.log.warn(__name__, '"2D675BA2" count1 is not 0')
		count2 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		for _ in range(count2):
			file_object_data_wrapper.read_str(2, out_file)
			file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		count3 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		self.transformation_matrix = []
		for _ in range(count3):  # transformation matrix
			self.transformation_matrix.append(file_object_data_wrapper.read_numpy(numpy.float32, 64, out_file, indent_count))
			file_object_data_wrapper.out_file_write('\n', out_file, indent_count)

		count4 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		for _ in range(count4):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)