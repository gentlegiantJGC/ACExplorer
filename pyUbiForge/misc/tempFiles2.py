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
	def file(self) -> FileObjectDataWrapper:
		"""The raw data wrapped up in a custom data wrapper.
		See FileObjectDataWrapper for more information.
		"""
		return FileObjectDataWrapper.from_binary(self._pyUbiForge, self._raw_file)


class LastUsed:
	def __init__(self):
		self._position_to_data = {}
		self._data_to_position = {}
		self._min = 0
		self._max = 0

	def remove(self, data: int):
		if data in self._data_to_position:
			position = self._data_to_position[data]
			del self._data_to_position[data]
			del self._position_to_data[position]

	def pop(self):
		while self._min not in self._position_to_data and self._min < self._max:
			self._min += 1
		if self._min == self._max:
			return
		else:
			data = self._position_to_data[self._min]
			del self._position_to_data[self._min]
			del self._data_to_position[data]
			return data

	def append(self, data: int):
		self._position_to_data[self._max] = data
		self._data_to_position[data] = self._max
		self._max += 1

	def clear(self):
		self._position_to_data.clear()
		self._data_to_position.clear()
		self._min = 0
		self._max = 0


class LightDictionary:
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self._light_dictionary = {}
		self._changed = False
		self._forge_to_index = {}
		self._index_to_forge = {}
		self._max_forge_index = 0

	@property
	def changed(self):
		return self._changed

	def load(self):
		"""Load the light dictionary file from disk into memory if it exists."""
		self.clear()
		if os.path.isfile(f'./resources/lightDict/{self.pyUbiForge.game_functions.game_identifier}.json'):
			with open(f'./resources/lightDict/{self.pyUbiForge.game_functions.game_identifier}.json', 'r') as light_dict:
				self._light_dictionary = json.load(light_dict)
			self._forge_to_index = self._light_dictionary['forge_index']
			self._max_forge_index = len(self._forge_to_index)
			del self._light_dictionary['forge_index']
			self._index_to_forge = {val: key for key, val in self._forge_to_index.items()}

	def save(self):
		"""Save the light dictionary in memory back to disk if it has changed."""
		if self.changed:
			if not os.path.isdir('./resources/lightDict'):
				os.makedirs('./resources/lightDict')
			temp_light_dict = self._light_dictionary
			temp_light_dict['forge_index'] = self._forge_to_index
			with open(f'./resources/lightDict/{self.pyUbiForge.game_functions.game_identifier}.json', 'w') as f:
				json.dump(temp_light_dict, f)

	def clear(self):
		self._light_dictionary.clear()
		self._changed = False
		self._forge_to_index.clear()
		self._index_to_forge.clear()
		self._max_forge_index = 0

	def get(self, file_id: int, forge_file_name: str = None) -> Union[int, None]:
		file_id = self.int_to_base64(file_id)
		if forge_file_name is not None:
			forge_file_name = self._forge_to_index[forge_file_name]
		if file_id in self._light_dictionary:
			if forge_file_name is not None and forge_file_name in self._light_dictionary[file_id]:
				return self._light_dictionary[file_id][0]
			else:
				forge_file_name = list(self._light_dictionary[file_id].keys())[0]
				return self._light_dictionary[file_id][forge_file_name][0]
		else:
			return None

	def add(self, file_id: int, forge_file_name: str, datafile_id: int):
		file_id = self.int_to_base64(file_id)
		datafile_id = self.int_to_base64(datafile_id)
		if forge_file_name not in self._forge_to_index:
			self._forge_to_index[forge_file_name] = self.int_to_base64(self._max_forge_index)
			self._index_to_forge[self._forge_to_index[forge_file_name]] = forge_file_name
			self._max_forge_index += 1
		forge_file_name = self._forge_to_index[forge_file_name]
		if file_id not in self._light_dictionary:
			self._light_dictionary[file_id] = {}
		if forge_file_name not in self._light_dictionary[file_id]:
			self._light_dictionary[file_id][forge_file_name] = []
		if datafile_id not in self._light_dictionary[file_id][forge_file_name]:
			self._light_dictionary[file_id][forge_file_name].append(datafile_id)
			self._changed = True

	@staticmethod
	def int_to_base64(inp: int) -> str:
		if inp == 0:
			return 'A'
		output = []
		table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
		while inp > 0:
			output.insert(0, table[inp & 63])
			inp = inp >> 6
		return ''.join(output)

	@staticmethod
	def base64_to_int(inp: str) -> int:
		output = 0
		table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63}
		for c in inp:
			output = output << 6
			output += table[c]
		return output


class TempFilesContainer:
	"""Class to hold all the files and the methods to access them and pull them from the original files."""
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		# dictionary to look up which dataFile a fileID is contained in (if it itself is not the main file in the dataFile)
		self._light_dictionary = LightDictionary(py_ubi_forge)
		# the amount of memory self.rawFiles takes (used to remove files)
		self._memory = 0
		# a dictionary of every file currently loaded into memory
		self._temp_files = {}
		self._last_used = LastUsed()

	@property
	def light_dict_changed(self) -> bool:
		return self._light_dictionary.changed

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
			remove_entry = self._last_used.pop()
			self._memory -= len(self._temp_files[remove_entry][4])
			del self._temp_files[remove_entry]

		if file_id != datafile_id:
			self._light_dictionary.add(file_id, forge_file_name, datafile_id)

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
				else:
					datafile_id = self._light_dictionary.get(file_id, forge_file_name)
					if datafile_id is None:
						forge_file_name = None

		if forge_file_name is None:
			forge_file_name = next((fF for fF in self.pyUbiForge.forge_files.keys() if file_id in self.pyUbiForge.forge_files[fF].datafiles), None)
			if forge_file_name is None:
				datafile_id = self._light_dictionary.get(file_id)
				if datafile_id is None:
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
		if self._light_dictionary.changed:
			self.save()
		self._light_dictionary.clear()
		self._memory = 0
		self._temp_files.clear()
		self._last_used.clear()

	def refresh_usage(self, file_id: int):
		"""Mark file_id as recently used so that it is not unloaded if the memory limit is reached."""
		if file_id in self._temp_files:
			self._last_used.remove(file_id)
		self._last_used.append(file_id)

	def save(self):
		self._light_dictionary.save()

	def load(self):
		self._light_dictionary.load()
