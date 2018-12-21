from typing import Dict, List

"""
All the code needed to access the raw files from a .forge file
"""


class DataFile:
	def __init__(self, raw_data_offset: int, raw_data_size: int, file_name: str):
		self._raw_data_offset = raw_data_offset
		self._raw_data_size = raw_data_size
		self._file_name = file_name
		self._files = {}

	@property
	def raw_data_offset(self) -> int:
		return self._raw_data_offset

	@property
	def raw_data_size(self) -> int:
		return self._raw_data_size

	@property
	def file_name(self) -> str:
		return self._file_name

	@property
	def files(self) -> Dict[int, str]:
		return self._files


class BaseForge:
	def __init__(self, ac_explorer_main, path: str, forge_file_name: str):
		self.ACExplorer_main = ac_explorer_main
		self._forge_file_name = forge_file_name
		self._path = path
		self._datafiles = {}
		self._new_datafiles = []

	def decompress_datafile(self, file_id):
		return

	@property
	def forge_file_name(self) -> str:
		return self._forge_file_name

	@property
	def path(self) -> str:
		return self._path

	@property
	def datafiles(self) -> Dict[int, DataFile]:
		return self._datafiles

	@property
	def new_datafiles(self) -> List[int]:
		return self._new_datafiles


def read_file_header(file_object_data_wrapper, out_file, indent_count):
	return
