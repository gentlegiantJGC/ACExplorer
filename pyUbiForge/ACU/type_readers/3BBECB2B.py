from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import logging


class Reader(BaseReader):
	file_type = '3BBECB2B'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(11)
		count1 = file_object_data_wrapper.read_uint_32()
		for _ in range(count1):
			file_object_data_wrapper.read_file()

		# 1.1 in float
		# 4 bytes
		# count
		# 00
		# fileID
		# 1.5 in float

		# 2.1 in float
		# count?
		# 00
		# fileID
		# 4 bytes
		# 3 in float
		# count
		# 00
		# fileID
		# count
		# 00
		# fileID

		file_object_data_wrapper.read_bytes(4)  # float
		for _ in range(2):
			count2 = file_object_data_wrapper.read_uint_32()
			if count2 > 10000:
				logging.warning('error reading entity file')
				# convert to an actual logger
				raise Exception()
			for _ in range(count2):
				file_object_data_wrapper.read_bytes(1)
				file_object_data_wrapper.read_id()
		file_object_data_wrapper.out_file_write('\n')
