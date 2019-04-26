from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'DAB4219F'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		pass
