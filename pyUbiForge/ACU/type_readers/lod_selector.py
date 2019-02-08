from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '01437462'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_str(1, out_file)
		file_object_data_wrapper.read_id(out_file, indent_count)
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		for _ in range(5):
			ending0 = file_object_data_wrapper.read_str(1, out_file)
			if ending0 == '00':
				py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
			elif ending0 != '03':
				raise Exception()
	# while ending0 == '00':
	#
	# 	ending0 = file_object_data_wrapper.read_str(1, out_file)
	# while ending0 == '03':
	# 	ending0 = file_object_data_wrapper.read_str(1, out_file)
