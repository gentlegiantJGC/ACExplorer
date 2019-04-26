from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
from typing import List
from pyUbiForge.ACU.type_readers.D77FB524 import Reader as Fake


class Reader(BaseReader):
	file_type = 'C69A7F31'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		fake_count = file_object_data_wrapper.read_uint_32()
		self.fakes: List[Fake] = []
		for _ in range(fake_count):
			self.fakes.append(
				file_object_data_wrapper.read_file()
			)
		near_fake_count = file_object_data_wrapper.read_uint_32()
		self.near_fakes = []
		for _ in range(near_fake_count):
			self.near_fakes.append(
				file_object_data_wrapper.read_file()
			)
		file_object_data_wrapper.read_bytes(1)
