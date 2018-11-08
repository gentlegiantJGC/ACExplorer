import pkgutil
import importlib
import sys


class RightClickLoader:
	"""
	the following are required in a plugin for it to be loaded
	plugin_name = 'Plugin Name'  # the name shown to the user
	plugin_level = integer 1, 2 or 4  # this is the level in the file tree this plugin applies to.
		1 - the top entry
		2 - the forge file
		3 - the datafile (for plugins specific to a certain file type use 4, those will appear here as well)
		4 - the specific file in the datafile and the parent datafile with the same id
			if plugin_level == 4 then the big endian hex string representation of the file type must be given
			file_type = '415D9568'
	def plugin(app, file_id):
		# plugin code here
	"""
	def __init__(self, app):
		self.app = app
		self.game_identifier = ''
		self.plugins = {1: [], 2: [], 3: [], 4: {}}

	def get(self, depth, file_id):
		if self.app.gameFunctions.gameIdentifier != self.game_identifier:
			self.game_identifier = self.app.gameFunctions.gameIdentifier
			self.plugins = {1: [], 2: [], 3: [], 4: {}}
			self.load_plugins()
		if depth in [1, 2]:
			return self.plugins[depth], file_id
		elif depth == 3:
			file_id = int(file_id)
			return list(set(self.plugins[3] + self.plugins[4].get(self.app.tempNewFiles.getData(file_id)['fileType'], []))), file_id
		elif depth == 4:
			file_id = int(file_id)
			return self.plugins[4].get(self.app.tempNewFiles.getData(file_id)['fileType'], []), file_id

	def load_plugins(self):
		for finder, name, _ in pkgutil.iter_modules([f'./ACExplorer/{self.app.gameFunctions.gameIdentifier}/right_click_methods']):
			module = load_module(name, finder.path)
			if not hasattr(module, 'plugin_name'):
				self.app.log.warn(__name__, f'Failed loading {name} because "plugin_name" was not defined')
				continue
			elif not isinstance(module.plugin_name, str):
				self.app.log.warn(__name__, f'Failed loading {name} because "plugin_name" was not a string')
				continue

			if not hasattr(module, 'plugin_level'):
				self.app.log.warn(__name__, f'Failed loading {name} because "plugin_level" was not defined')
				continue
			elif not (isinstance(module.plugin_level, int) and module.plugin_level in [1, 2, 3, 4]):
				self.app.log.warn(__name__, f'Failed loading {name} because "plugin_level" was not an int in [1,2,3,4]')
				continue
			if module.plugin_level == 4:
				if not hasattr(module, 'file_type'):
					self.app.log.warn(__name__, f'Failed loading {name} because "file_type" was not defined')
					continue
				elif not isinstance(module.file_type, str):
					self.app.log.warn(__name__, f'Failed loading {name} because "file_type" was not a string')
					continue

			if not hasattr(module, 'plugin'):
				self.app.log.warn(__name__, f'Failed loading {name} because "plugin" was not defined')
				continue

			if module.plugin_level in [1, 2, 3]:
				self.plugins[module.plugin_level].append(module)
			else:
				if module.file_type not in self.plugins[module.plugin_level]:
					self.plugins[module.plugin_level][module.file_type] = []
				self.plugins[module.plugin_level][module.file_type].append(module)
			self.app.log.info(__name__, f'Successfully loaded right click plugin: "{module.plugin_name}"')


class DataTypeLoader:
	def __init__(self, app):
		pass


def load_module(name, path):
	module_spec = importlib.util.spec_from_file_location(name, f'{path}/{name}.py')
	module = importlib.util.module_from_spec(module_spec)
	module_spec.loader.exec_module(module)
	return module
