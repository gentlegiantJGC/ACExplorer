"""
	This is a package containing code to access the files from .forge files used by the Anvil game engine
	to store all assets used in the game. It also contains code to extract information from the files when
	they have been decompressed. The format varies slightly between games and the current implementation
	will only work with Assassin's Creed Unity.

	The forge file format is similar to a zip file in concept with folders in the main directory and binary
	files contained within each directory.
	The 'folders' in the top level of the forge file will from this point on be referred to as 'datafiles'.
	The files contained within the datafile all relate to that datafile but vary in format.
"""

import os
from typing import Union, Dict
from pyUbiForge import ACU, misc
from pyUbiForge.misc.forge import BaseForge

games = {
	'ACU': ACU
}


class PyUbiForgeMain:
	"""This is the main class that holds all the data for this package.

	To initiate the package first import it then create an instance of this class.
	All the methods needed are either defined here or can be found within objects defined here.
	"""
	def __init__(self):
		self._CONFIG = misc.Config()
		self._game_functions = None
		self._log = misc.Logger(self)
		self._temp_files = misc.TempFilesContainer(self)
		self._right_click_plugins = misc.plugins.PluginHandler(self)
		self._read_file = misc.file_readers.FileReaderHandler(self)
		self._forge_files = {}  # _forge_files is a dictionary mapping from str name of the forge file to a Forge class.

	@property
	def CONFIG(self) -> misc.Config:
		"""Returns the config class with data from config.json loaded if it exists."""
		return self._CONFIG

	@property
	def game_functions(self):
		"""Returns the package for the loaded game or None if load_game has not been called."""
		return self._game_functions

	@property
	def log(self) -> misc.Logger:
		"""Returns the logging class."""
		return self._log

	@property
	def temp_files(self) -> misc.TempFilesContainer:
		"""Returns the temp_files class where all decompressed data is stored.

		If you want a file, request it from this class and it will look for it, decompress it
		if it exists, and return it. It will also deal with cleanup when nearing the memory cap.
		"""
		return self._temp_files

	@property
	def right_click_plugins(self) -> misc.plugins.PluginHandler:
		"""Returns a class that stores right click methods."""
		return self._right_click_plugins

	@property
	def read_file(self) -> misc.file_readers.FileReaderHandler:
		"""Returns a class containing the code to read data from the files."""
		return self._read_file

	@property
	def game_identifier(self) -> Union[str, None]:
		"""Returns the game identifier for the game currently loaded.

		Returns None if load_game has not been called.
		"""
		if self.game_functions is not None:
			if hasattr(self.game_functions, 'game_identifier'):
				return self.game_functions.game_identifier
			else:
				raise AttributeError
		else:
			return None

	@property
	def forge_files(self) -> Dict[str, BaseForge]:
		"""Returns the dictionary mapping file name string to Forge class."""
		return self._forge_files

	def load_game(self, game_identifier: str):
		"""Call this with the identifier of the game you want to load.

		This needs to be run after startup as no game is loaded to begin with
		This is also what you should call if you want to switch between games.
		Valid identifiers are defined in games at the top of this file.
		"""
		self.log.info(__name__, 'Loading Game Files.')
		self.temp_files.clear()
		if game_identifier in games:
			self._game_functions = games.get(game_identifier)
			if os.path.isdir(self.CONFIG.game_folder(game_identifier)):
				self._forge_files = {
					forge_file_name: self.game_functions.forge.Forge(
						self,
						os.path.join(self.CONFIG.game_folder(game_identifier), forge_file_name),
						forge_file_name
					) for forge_file_name in os.listdir(
						self.CONFIG.game_folder(game_identifier)
					) if forge_file_name.endswith('.forge')
				}
			else:
				self._forge_files = {}

			self.temp_files.load()
		self.log.info(__name__, 'Finished Loading Game Files.')

	def save(self):
		"""Call this method to save the config file and light dictioary back to disk."""
		self.CONFIG.save()
		self.temp_files.save()
