from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '0E5A450A'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper):
		# readStr(fIn, fOut, 184)
		file_object_data_wrapper.read_bytes(14)
		for _ in range(2):
			py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper)
