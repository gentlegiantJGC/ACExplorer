from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import logging


class Reader(BaseReader):
	file_type = 'B88B305B'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		check = file_object_data_wrapper.read_uint_8()
		if check == 1:
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_id()
		elif check == 3:
			file_object_data_wrapper.read_bytes(9)
		else:
			logging.warning(f'Expected check to be 1 or 3 but got {check}')
			raise Exception

		file_object_data_wrapper.read_bytes(1)

		check = file_object_data_wrapper.read_uint_8()
		if check == 1:
			file_object_data_wrapper.read_bytes(1)
			file_object_data_wrapper.read_id()
		elif check == 3:
			file_object_data_wrapper.read_bytes(9)
		else:
			logging.warning(f'Expected check to be 1 or 3 but got {check}')
			raise Exception
