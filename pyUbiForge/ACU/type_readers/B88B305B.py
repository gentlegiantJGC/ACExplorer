from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'B88B305B'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		check = file_object_data_wrapper.read_uint_8(out_file, indent_count)
		if check == 1:
			file_object_data_wrapper.read_bytes(1, out_file, indent_count)
			file_object_data_wrapper.read_id(out_file, indent_count)
		elif check == 3:
			file_object_data_wrapper.read_bytes(9, out_file, indent_count)
		else:
			py_ubi_forge.log.warn(__name__, f'Expected check to be 1 or 3 but got {check}')
			raise Exception

		file_object_data_wrapper.read_bytes(1, out_file, indent_count)

		check = file_object_data_wrapper.read_uint_8(out_file, indent_count)
		if check == 1:
			file_object_data_wrapper.read_bytes(1, out_file, indent_count)
			file_object_data_wrapper.read_id(out_file, indent_count)
		elif check == 3:
			file_object_data_wrapper.read_bytes(9, out_file, indent_count)
		else:
			py_ubi_forge.log.warn(__name__, f'Expected check to be 1 or 3 but got {check}')
			raise Exception
