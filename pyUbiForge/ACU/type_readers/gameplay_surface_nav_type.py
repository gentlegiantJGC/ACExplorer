from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '1C4B22AA'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(6, out_file, indent_count)
		b = file_object_data_wrapper.read_uint_8(out_file, indent_count)
		if b == 3:
			file_object_data_wrapper.read_bytes(5, out_file, indent_count)
			file_object_data_wrapper.read_id(out_file, indent_count)
		elif b == 5:
			file_object_data_wrapper.read_id(out_file, indent_count)
			file_object_data_wrapper.read_bytes(5, out_file, indent_count)
			file_object_data_wrapper.read_id(out_file, indent_count)
		else:
			py_ubi_forge.log.warn(__name__, 'value is not 3 or 5 I don\'t know how to deal with this')
