from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'EE568905'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		for n in range(count1):
			file_object_data_wrapper.read_str(1, out_file, indent_count + 1)
			fileID2 = file_object_data_wrapper.read_id(out_file, indent_count + 1)
			py_ubi_forge.game_functions.read_file(py_ubi_forge, fileID2)
			py_ubi_forge.log.info(__name__, f'{n} of {count1}')
