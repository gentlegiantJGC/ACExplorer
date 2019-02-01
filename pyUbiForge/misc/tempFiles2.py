import os
import json
from typing import Union
from pyUbiForge.misc.file_object import FileObjectDataWrapper

"""
Forge file
Forge1.forge
	dataFile1
		file1
		file2
		...
	dataFile2
		file1
		file2
		...
	dataFile3
		file1
		file2
		...
	...
Forge2.forge
	dataFile1
		file1
		file2
		...
	dataFile2
		file1
		file2
		...
	dataFile3
		file1
		file2
		...
	...
"""

"""
tempFiles
{
	<fileID>:(<forgeFile>, <datafileID>, <fileType>, <fileName>, None),
	...
}
"""

"""
lightDictionary
{
	fileID:{
		<forgeFile>:[]
	}
}
"""


class TempFile:
	def __init__(self, py_ubi_forge, forge_file: str, datafile_id: int, file_id: int, file_type: str, file_name: str, raw_file: bytes):
		"""Container for data related to a file.
		Should help with typing and argument selection compared to the old dictionary method
		"""
		self._pyUbiForge = py_ubi_forge
		self._forge_file = forge_file
		self._datafile_id = datafile_id
		self._file_id = file_id
		self._file_type = file_type
		self._file_name = file_name
		self._raw_file = raw_file

	@property
	def forge_file(self) -> str:
		"""The name of the forge file the file is contained in."""
		return self._forge_file

	@property
	def datafile_id(self) -> int:
		"""The numerical id of the datafile the file is contained in.
		In some cases this may be the same as the file_id since every datafile will have containing file with the same id.
		"""
		return self._datafile_id

	@property
	def file_id(self) -> int:
		"""The numerical file id relating to the file.
		Theoretically this is unique to that file but there are some duplicates.
		From what I can tell all files with the same id contain the same data.
		"""
		return self._file_id

	@property
	def file_type(self) -> str:
		"""The big endian hexadecimal representation of the file type."""
		return self._file_type

	@property
	def file_name(self) -> str:
		"""The name of the file"""
		return self._file_name

	@property
	def file_object_data_wrapper(self) -> FileObjectDataWrapper:
		"""The raw data wrapped up in a custom data wrapper.
		See FileObjectDataWrapper for more information.
		"""
		return FileObjectDataWrapper.from_binary(self._pyUbiForge, self._raw_file)


class TempFilesContainer:
	"""Class to hold all the files and the methods to access them and pull them from the original files."""
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		# dictionary to look up which dataFile a fileID is contained in (if it itself is not the main file in the dataFile)
		self._light_dictionary = {}
		self._light_dict_changed = False
		# the amount of memory self.rawFiles takes (used to remove files)
		self._memory = 0
		# a dictionary of every file currently loaded into memory
		self._temp_files = {}
		self._last_used = []

	@property
	def light_dict_changed(self) -> bool:
		return self._light_dict_changed

	def add(self, file_id: int, forge_file_name: str, datafile_id: int, file_type: int, file_name: str, raw_file: bytes = None):
		"""
		:param file_id: int
		:param forge_file_name: str
		:param datafile_id: int of containing datafile
		:param file_type: int
		:param file_name: str
		:param raw_file: binary
		"""
		if file_id in self._temp_files:
			self._memory -= len(self._temp_files[file_id][4])
		self.refresh_usage(file_id)
		self._temp_files[file_id] = (forge_file_name, datafile_id, file_type, file_name, raw_file)
		if raw_file is not None:
			self._memory += len(raw_file)

		while self._memory > self.pyUbiForge.CONFIG['tempFilesMaxMemoryMB']*1000000:
			remove_entry = self._last_used.pop(0)
			self._memory -= len(self._temp_files[remove_entry][4])
			del self._temp_files[remove_entry]

		if file_id != datafile_id:
			if str(file_id) not in self._light_dictionary:
				self._light_dictionary[str(file_id)] = {}
			if forge_file_name not in self._light_dictionary[str(file_id)]:
				self._light_dictionary[str(file_id)][forge_file_name] = []
			if datafile_id not in self._light_dictionary[str(file_id)][forge_file_name]:
				self._light_dictionary[str(file_id)][forge_file_name].append(datafile_id)
				self._light_dict_changed = True

	def __call__(self, file_id: int, forge_file_name: str = None, datafile_id: int = None) -> Union[None, TempFile]:
		"""Tries to find the file matching the description and return a TempFile class containing the data.
		Returns None if it cannot find the file.
		:param file_id: int
		:param forge_file_name: str
		:param datafile_id: int of the containing datafile
		:return: TempFile, None
		"""

		if forge_file_name is not None and datafile_id is None:
			if file_id in self._temp_files and forge_file_name == self._temp_files[file_id][0]:
				datafile_id = self._temp_files[file_id][1]
			else:
				# preferentially use one found in the forgeFile asked but look in others if needed
				if forge_file_name in self.pyUbiForge.forge_files and file_id in self.pyUbiForge.forge_files[forge_file_name].datafiles:
					datafile_id = file_id
				elif str(file_id) in self._light_dictionary and forge_file_name in self._light_dictionary[str(file_id)]:
					datafile_id = self._light_dictionary[str(file_id)][0]
				else:
					forge_file_name = None
		if forge_file_name is None:
			forge_file_name = next((fF for fF in self.pyUbiForge.forge_files.keys() if file_id in self.pyUbiForge.forge_files[fF].datafiles), None)
			if forge_file_name is None:
				if str(file_id) in self._light_dictionary:  # could check the lower down stuff but if this exists there should be data inside
					forge_file_name = next(iter(self._light_dictionary[str(file_id)]))
					datafile_id = self._light_dictionary[str(file_id)][forge_file_name][0]
				else:
					return
			else:
				datafile_id = file_id

		if not (file_id in self._temp_files and forge_file_name == self._temp_files[file_id][0] and datafile_id == self._temp_files[file_id][1]):
			self.pyUbiForge.forge_files[forge_file_name].decompress_datafile(datafile_id)
		self.refresh_usage(file_id)
		if file_id in self._temp_files and forge_file_name == self._temp_files[file_id][0] and datafile_id == self._temp_files[file_id][1]:
			return TempFile(
				self.pyUbiForge,
				forge_file_name,
				datafile_id,
				file_id,
				f'{self._temp_files[file_id][2]:08X}',
				self._temp_files[file_id][3],
				self._temp_files[file_id][4]
			)
		else:
			return

	def clear(self):
		"""Resets the TempFilesContainer class back to its starting state.
		Used when opening loading a new game.
		"""
		if self._light_dict_changed:
			self.save()
		self._light_dictionary.clear()
		self._memory = 0
		self._temp_files.clear()
		self._last_used = []
		self._light_dict_changed = False

	def refresh_usage(self, file_id):
		"""Mark file_id as recently used so that it is not unloaded if the memory limit is reached."""
		if file_id in self._temp_files:
			self._last_used.remove(file_id)
		self._last_used.append(file_id)

	def save(self):
		"""Save the light dictionary in memory back to disk if it has changed."""
		if self.light_dict_changed:
			if not os.path.isdir('./resources/lightDict'):
				os.makedirs('./resources/lightDict')
			with open(f'./resources/lightDict/{self.pyUbiForge.game_functions.game_identifier}.json', 'w') as f:
				json.dump(self._light_dictionary, f)

	def load(self):
		"""Load the light dictionary file from disk into memory if it exists."""
		if os.path.isfile(f'./resources/lightDict/{self.pyUbiForge.game_functions.game_identifier}.json'):
			with open(f'./resources/lightDict/{self.pyUbiForge.game_functions.game_identifier}.json', 'r') as light_dict:
				self._light_dictionary = json.load(light_dict)
