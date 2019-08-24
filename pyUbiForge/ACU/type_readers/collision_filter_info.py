from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '43EF99C2'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(15)  # previously 17
		file_object_data_wrapper.out_file_write('\n')


		"""
		01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00
		00 00 80 3F 00 00 7A 44 00 00 A0 41 CD CC 4C 3D CD CC CC 3D 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
		"""

		"""
		01 00 00 00 00 00 00 00 00 00 00 00 00 00 00
		trmMtx
		"""