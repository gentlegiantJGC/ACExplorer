import pkgutil
import importlib
from pyUbiForge.misc.file_object import FileObjectDataWrapper


class RightClickHandler:
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
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self.game_identifier = ''
		self.plugins = {1: [], 2: [], 3: [], 4: {'*': []}}

	def get(self, depth, file_id, forge_file_name=None, datafile_id=None):
		if self.pyUbiForge.game_functions.game_identifier != self.game_identifier:
			self.game_identifier = self.pyUbiForge.game_functions.game_identifier
			self.plugins = {1: [], 2: [], 3: [], 4: {'*': []}}
			self.load_plugins()
		if depth in [1, 2]:
			return self.plugins[depth], file_id
		elif depth == 3:
			file_id = int(file_id)
			return list(set(self.plugins[3] + self.plugins[4].get(self.pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)['fileType'], []) + self.plugins[4]['*'])), file_id
		elif depth == 4:
			file_id = int(file_id)
			return self.plugins[4].get(self.pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)['fileType'], []) + self.plugins[4]['*'], file_id

	def load_plugins(self):
		for finder, name, _ in pkgutil.iter_modules([f'./ACExplorer/{self.pyUbiForge.game_functions.game_identifier}/right_click_methods']):
			module = load_module(name, finder.path)
			if not hasattr(module, 'plugin_name'):
				self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin_name" was not defined')
				continue
			elif not isinstance(module.plugin_name, str):
				self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin_name" was not a string')
				continue

			if not hasattr(module, 'plugin_level'):
				self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin_level" was not defined')
				continue
			elif not (isinstance(module.plugin_level, int) and module.plugin_level in [1, 2, 3, 4]):
				self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin_level" was not an int in [1,2,3,4]')
				continue
			if module.plugin_level == 4:
				if not hasattr(module, 'file_type'):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not defined')
					continue
				elif not isinstance(module.file_type, str):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not a string')
					continue

			if not hasattr(module, 'plugin'):
				self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin" was not defined')
				continue

			if module.plugin_level in [1, 2, 3]:
				self.plugins[module.plugin_level].append(module)
			else:
				if module.file_type not in self.plugins[module.plugin_level]:
					self.plugins[module.plugin_level][module.file_type] = []
				self.plugins[module.plugin_level][module.file_type].append(module)
			self.pyUbiForge.log.info(__name__, f'Successfully loaded right click plugin: "{module.plugin_name}"')


class DataTypeHandler:
	def __init__(self, app):
		self.app = app
		self.game_identifier = ''
		self.plugins = {}

	def __call__(self, file_object_data_wrapper, out_file=None, indent_count=0):
		"""
		Call this function in the right click methods as the start point
		Will call get_data_recursive to get the actual data followed by the clever_format method to read the rest of the file
		:param file_object_data_wrapper:
		:param out_file:
		:param indent_count:
		:return: objects defined in the plugins
		"""
		if self.app.game_functions.game_identifier != self.game_identifier:
			self.game_identifier = self.app.game_functions.game_identifier
			self.plugins = {}
			self.load_plugins()
		if not isinstance(file_object_data_wrapper, FileObjectDataWrapper):
			raise Exception('file_object_data_wrapper is not of type FileObjectDataWrapper')
		data = self.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		file_object_data_wrapper.clever_format(out_file, indent_count)
		return data

	def get_data_recursive(self, file_object_data_wrapper, out_file, indent_count):
		"""
		Call this function in file reader methods to access other file types in the same file
		:param file_object_data_wrapper:
		:param out_file:
		:param indent_count:
		:return:
		"""
		file_type = self.app.game_functions.forge.read_file_header(file_object_data_wrapper, out_file, indent_count)
		if file_type in self.plugins:
			return self.plugins[file_type](self.app, file_object_data_wrapper, out_file, indent_count+1)
		else:
			raise Exception(f'File type {file_type} does not have a file reader')

	def load_plugins(self):
		for finder, name, _ in pkgutil.iter_modules([f'./ACExplorer/{self.app.game_functions.game_identifier}/type_readers']):
			plugin = load_module(name, finder.path)

			if not hasattr(plugin, 'file_type'):
				self.app.log.warn(__name__, f'Failed loading {name} because "file_type" was not defined')
				continue
			elif not isinstance(plugin.file_type, str):
				self.app.log.warn(__name__, f'Failed loading {name} because "file_type" was not a string')
				continue
			try:
				file_type = plugin.file_type
			except Exception as e:
				self.app.log.warn(__name__, f'Failed loading {name} because parsing of "file_type" failed\n{e}')
				continue

			if not hasattr(plugin, 'plugin'):
				self.app.log.warn(__name__, f'Failed loading {name} because "plugin" was not defined')
				continue

			if file_type in self.plugins:
				self.app.log.warn(__name__, f'Skipping plugin "{name}" because a reader for this file type was already found')
				continue
			else:
				self.plugins[file_type] = plugin.plugin


def load_module(name, path):
	module_spec = importlib.util.spec_from_file_location(name, f'{path}/{name}.py')
	module = importlib.util.module_from_spec(module_spec)
	module_spec.loader.exec_module(module)
	return module
