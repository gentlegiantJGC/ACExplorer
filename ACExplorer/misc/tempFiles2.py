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


class TempFilesContainer:
	def __init__(self, app):
		self.app = app
		# dictionary to look up which dataFile a fileID is contained in (if it itself is not the main file in the dataFile)
		self.light_dictionary = {}
		self._light_dict_changed = False
		# the amount of memory self.rawFiles takes (used to remove files)
		self._memory = 0
		# a dictionary of every file currently loaded into memory
		self._temp_files = {}
		self._last_used = []

	@property
	def light_dict_changed(self):
		return self._light_dict_changed

	def add(self, file_id, forge_file_name, datafile_id, file_type, file_name, raw_file=None):
		"""
		:param file_id: int
		:param forge_file_name: str
		:param datafile_id: int of containing datafile
		:param file_type: int
		:param file_name: str
		:param raw_file: binary
		:return:
		"""
		if file_id in self._temp_files:
			self._memory -= len(self._temp_files[file_id][4])
		self.refresh_usage(file_id)
		self._temp_files[file_id] = (forge_file_name, datafile_id, file_type, file_name, raw_file)
		if raw_file is not None:
			self._memory += len(raw_file)

		while self._memory > self.app.CONFIG['tempFilesMaxMemoryMB']*1000000:
			remove_entry = self._last_used.pop(0)
			self._memory -= len(self._temp_files[remove_entry][4])
			del self._temp_files[remove_entry]

		if file_id != datafile_id:
			if str(file_id) not in self.light_dictionary:
				self.light_dictionary[str(file_id)] = {}
			if forge_file_name not in self.light_dictionary[str(file_id)]:
				self.light_dictionary[str(file_id)][forge_file_name] = []
			if datafile_id not in self.light_dictionary[str(file_id)][forge_file_name]:
				self.light_dictionary[str(file_id)][forge_file_name].append(datafile_id)
				self._light_dict_changed = True

	def __call__(self, file_id, forge_file_name=None, datafile_id=None):
		"""
		:param file_id: int
		:param forge_file_name: str
		:param datafile_id: int of the containing datafile
		:return:
		"""

		if forge_file_name is not None and datafile_id is None:
			if file_id in self._temp_files and forge_file_name == self._temp_files[file_id][0]:
				datafile_id = self._temp_files[file_id][1]
			else:
				# preferentially use one found in the forgeFile asked but look in others if needed
				if forge_file_name in self.app.file_list and file_id in self.app.file_list[forge_file_name]:
					datafile_id = file_id
				elif str(file_id) in self.light_dictionary and forge_file_name in self.light_dictionary[str(file_id)]:
					datafile_id = self.light_dictionary[str(file_id)][0]
				else:
					forge_file_name = None
		if forge_file_name is None:
			forge_file_name = next((fF for fF in self.app.file_list if file_id in self.app.file_list[fF]), None)
			if forge_file_name is None:
				if str(file_id) in self.light_dictionary:  # could check the lower down stuff but if this exists there should be data inside
					forge_file_name = next(iter(self.light_dictionary[str(file_id)]))
					datafile_id = self.light_dictionary[str(file_id)][forge_file_name][0]
				else:
					return
			else:
				datafile_id = file_id

		if not (file_id in self._temp_files and forge_file_name == self._temp_files[file_id][0] and datafile_id == self._temp_files[file_id][1]):
			self.app.gameFunctions.framework.decompress_datafile(self.app, datafile_id, forge_file_name)
		self.refresh_usage(file_id)
		if file_id in self._temp_files and forge_file_name == self._temp_files[file_id][0] and datafile_id == self._temp_files[file_id][1]:
			return {
				'forgeFile': forge_file_name,
				'datafileID': datafile_id,
				'fileType': f'{self._temp_files[file_id][2]:08X}',
				'fileName': self._temp_files[file_id][3],
				'rawFile': self.app.misc.file_object.FileObjectDataWrapper.from_binary(self.app, self._temp_files[file_id][4])
			}
		else:
			return

	def clear(self):
		self.light_dictionary.clear()
		self._memory = 0
		self._temp_files.clear()
		self._last_used = []
		self._light_dict_changed = False

	def refresh_usage(self, file_id):
		if file_id in self._temp_files:
			self._last_used.remove(file_id)
		self._last_used.append(file_id)
