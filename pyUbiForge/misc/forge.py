from typing import Dict, List, Union, TextIO
from pyUbiForge.misc.file_object import FileObjectDataWrapper

"""All the code needed to access the raw files from a .forge file."""


class DataFile:
	"""This class houses data for each datafile. It stores the name of the datafile and the files contained within."""
	def __init__(self, raw_data_offset: int, raw_data_size: int, file_name: str, file_type: int):
		self._raw_data_offset = raw_data_offset
		self._raw_data_size = raw_data_size
		self._file_name = file_name
		self._file_type = file_type
		self._files = {}

	@property
	def raw_data_offset(self) -> int:
		"""The number of bytes into the forge file that this datafile can be found."""
		return self._raw_data_offset

	@property
	def raw_data_size(self) -> int:
		"""The size of the datafile in bytes as found in the forge file."""
		return self._raw_data_size

	@property
	def file_name(self) -> str:
		"""The name associated with this forge file."""
		return self._file_name

	@property
	def file_type(self) -> str:
		"""The name associated with this forge file."""
		return self._file_type

	@property
	def files(self) -> Dict[int, str]:
		"""A dictionary mapping from file_id to string name for each file in the datafile.

		This will be an empty dictionary until the datafile is decompressed."""
		return self._files


class BaseForge:
	"""This class is the base class of Forge that all implementations should inherit from.

	It sets up all the variables and accessors for the variables.
	"""
	def __init__(self, py_ubi_forge, path: str, forge_file_name: str):
		self.pyUbiForge = py_ubi_forge
		self._forge_file_name = forge_file_name
		self._path = path
		self._datafiles = {}
		self._new_datafiles = []

	def decompress_datafile(self, file_id):
		raise NotImplemented

	@property
	def forge_file_name(self) -> str:
		"""The file name of the forge file."""
		return self._forge_file_name

	@property
	def path(self) -> str:
		"""The directory path to the forge file."""
		return self._path

	@property
	def datafiles(self) -> Dict[int, DataFile]:
		"""A dictionary mapping from datafile id to DataFile class."""
		return self._datafiles

	@property
	def new_datafiles(self) -> List[int]:
		"""A list of datafile integer ids that have been decompressed but not acknowledged by the wrapper program.

		In the wrapper program read this data and then call new_datafiles.clear() to empty the list
		"""
		return self._new_datafiles


def read_file_header(file_object_data_wrapper: FileObjectDataWrapper, out_file: Union[FileObjectDataWrapper, TextIO], indent_count: int):
	raise NotImplemented
