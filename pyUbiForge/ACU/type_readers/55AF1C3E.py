from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '55AF1C3E'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		count1 = file_object_data_wrapper.read_uint_32()
		for _ in range(count1):
			file_object_data_wrapper.read_bytes(41)
		count2 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.read_bytes(12 * count2)
		for _ in range(2):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.out_file_write('\n')

		"""
		file_object_data_wrapper.read_bytes(2)
		count1 = file_object_data_wrapper.read_uint_32()

		if count1 > 100:
			logging.warning('error reading unknown file type')
			# convert to an actual logger
			return fileContainer
		for _ in range(count1):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.out_file_write('\n')

		count2 = file_object_data_wrapper.read_uint_32()
		if count2 > 100:
			logging.warning('error reading unknown file type')
			# convert to an actual logger
			return fileContainer
		for _ in range(count2):
			readStr(fIn, fOut, 12)
		file_object_data_wrapper.out_file_write('\n')
		"""
