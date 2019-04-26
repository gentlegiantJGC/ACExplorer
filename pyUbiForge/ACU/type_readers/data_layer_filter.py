from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'DB1D406E'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		count1 = file_object_data_wrapper.read_uint_32()  # count
		# more data follows this if count != 0
		for _ in range(count1):
			file_object_data_wrapper.read_file()
		file_object_data_wrapper.out_file_write('\n')
