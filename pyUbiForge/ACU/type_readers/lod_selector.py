from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = '01437462'

	def __init__(self, file_object_data_wrapper: FileObjectDataWrapper):
		file_object_data_wrapper.read_bytes(1)
		file_object_data_wrapper.read_id()
		file_object_data_wrapper.out_file_write('\n')
		self._lod = []
		for _ in range(5):
			ending0 = file_object_data_wrapper.read_uint_8()
			if ending0 == 0:
				self._lod.append(file_object_data_wrapper.read_file())
			elif ending0 == 3:
				self._lod.append(None)
			else:
				raise Exception()

	def __getitem__(self, index: int):
		return self._lod[index]
