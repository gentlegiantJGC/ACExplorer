import os
from typing import Union, Dict
from . import ACU, misc
from .misc.forge import BaseForge

games = {
	'ACU': ACU
}


class PyUbiForgeMain:
	def __init__(self):
		self._CONFIG = misc.Config()
		self._game_functions = None
		self._log = misc.Logger(self)
		self._temp_files = misc.TempFilesContainer(self)
		self._right_click_plugins = misc.file_loaders.RightClickHandler(self)
		self._read_file = misc.file_loaders.DataTypeHandler(self)

		# forge_files is a dictionary of each forge file on the first level and
		# each datafile on the second level under each forge file. This is used
		# as a cheap way to find the location a file is stored under.
		self._forge_files = {}

	@property
	def CONFIG(self):
		return self._CONFIG

	@property
	def game_functions(self):
		return self._game_functions

	@property
	def log(self):
		return self._log

	@property
	def temp_files(self):
		return self._temp_files

	@property
	def right_click_plugins(self):
		return self._right_click_plugins

	@property
	def read_file(self):
		return self._read_file

	@property
	def game_identifier(self) -> Union[str, None]:
		if self.game_functions is not None:
			if hasattr(self.game_functions, 'game_identifier'):
				return self.game_functions.game_identifier
			else:
				raise AttributeError
		else:
			return None

	@property
	def forge_files(self) -> Dict[str, BaseForge]:
		return self._forge_files

	def load_game(self, game_identifier: str):
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
