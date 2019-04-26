from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
from pyUbiForge.ACU.type_readers.entity import Reader as Entity


class Reader(BaseReader):
	file_type = 'D77FB524'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(2)
		self.entity: Entity = file_object_data_wrapper.read_file()
		count1 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.indent()
		for _ in range(count1):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.indent(-1)
		count2 = file_object_data_wrapper.read_uint_32()
		file_object_data_wrapper.indent()
		file_object_data_wrapper.read_bytes(4*count2)
		file_object_data_wrapper.indent(-1)
		file_object_data_wrapper.read_uint_32()  # coord 1
		file_object_data_wrapper.read_uint_32()  # coord 2
		file_object_data_wrapper.read_bytes(1)
