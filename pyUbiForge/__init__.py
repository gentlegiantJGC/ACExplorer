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
import logging
from typing import Union, Dict, List
from pyUbiForge.misc.forge import BaseForge
from pyUbiForge.misc.config import CONFIG
from pyUbiForge.misc.tempFiles2 import temp_files
from pyUbiForge.misc.file_readers import file_reader_handler
from pyUbiForge import ACU

games = {
	'ACU': ACU
}
game_functions = None
forge_files: Dict[str, BaseForge] = {}
read_file: file_reader_handler = file_reader_handler


def game_identifier() -> Union[str, None]:
	"""Returns the game identifier for the game currently loaded.

	Returns None if load_game has not been called.
	"""
	if game_functions is not None:
		if hasattr(game_functions, 'game_identifier'):
			return game_functions.game_identifier
		else:
			raise AttributeError
	else:
		return None


def game_identifiers() -> List[str]:
	return list(games.keys())


def load_game(game_identifier_: str):
	"""Call this with the identifier of the game you want to load.

	This needs to be run after startup as no game is loaded to begin with
	This is also what you should call if you want to switch between games.
	Valid identifiers are defined in games at the top of this file.
	"""
	global game_functions
	global forge_files
	if game_identifier_ != game_identifier():
		logging.info(f'Loading Game Files for {game_identifier_}.')
		temp_files.clear()
		if game_identifier_ in games:
			game_functions = games.get(game_identifier_)
			forge_files = {}
			if os.path.isdir(CONFIG.game_folder(game_identifier_)):
				for forge_file_name in os.listdir(CONFIG.game_folder(game_identifier_)):
					if forge_file_name.endswith('.forge'):
						forge_files[forge_file_name] = game_functions.forge.Forge(
							os.path.join(CONFIG.game_folder(game_identifier_), forge_file_name),
							forge_file_name
						)
						yield forge_file_name

			temp_files.load()
		logging.info('Finished Loading Game Files.')


def save():
	"""Call this method to save the config file and light dictionary back to disk."""
	CONFIG.save()
	temp_files.save()
