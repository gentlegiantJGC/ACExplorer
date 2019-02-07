import pkgutil
import importlib
from typing import Tuple, Union, TextIO, Any
from pyUbiForge.misc.file_object import FileObjectDataWrapper


class RightClickHandler:
	"""
	A class which loads all the code for right click methods. Below is the format for the plugins

	The following are required in a plugin for it to be loaded.
	plugin_name = 'Plugin Name'  # the name shown to the user
	plugin_level = integer 1, 2, 3 or 4  # this is the level in the file tree this plugin applies to.
		1 - the top entry
		2 - the forge file
		3 - the datafile (for plugins specific to a certain file type use 4, those will appear here as well)
		4 - the specific file in the datafile and the parent datafile with the same id
			if plugin_level == 4 then the big endian hex string representation of the file type must be given
			file_type = '415D9568'
	def plugin(py_ubi_forge, file_id, forge_file_name, datafile_id, options):
		# plugin code here
	"""
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self.game_identifier = None
		self.plugins = {1: {}, 2: {}, 3: {}, 4: {'*': {}}}
		self.plugin_names = {}
		"""
		self.plugins = {
			1: {
				"plugin_name": plugin_module
			}, 
			2: {}, 
			3: {}, 
			4: {
				'*': {}
				'FFFFFFFF': {
					"plugin_name_2": plugin_module
				}
			}
		}
		"""

	def query(self, plugin_level: int, file_id: str, forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None) -> Tuple[list, Union[str, int]]:
		"""
		Look up which plugins are relevant to the given entry and return their names in a list.
		Each plugin has a unique name which is used as the unique identifier. Give this name to the get function with the file information to run the plugin
		:param plugin_level: See plugin_level at the top
		:param file_id: The furthest down id in the list. (eg game identifier, forge file name, datafile id or actual file id)
		:param forge_file_name: The name of the forge file
		:param datafile_id: The integer value of the datafile
		:return:
		"""
		self._load_plugins()

		if plugin_level in (1, 2):
			return list(
				self.plugins[plugin_level].keys()
			), file_id

		elif plugin_level in (3, 4):
			file_id = int(file_id)
			file_type = self.pyUbiForge.temp_files(file_id, forge_file_name, datafile_id).file_type

			if plugin_level == 3:
				return list(set(
					list(self.plugins[3].keys()) + list(self.plugins[4].get(file_type, {}).keys()) + list(self.plugins[4]['*'].keys())
				)), file_id

			elif plugin_level == 4:
				return list(set(
					list(self.plugins[4].get(file_type, {}).keys()) + list(self.plugins[4]['*'].keys())
				)), file_id

	def run(self, plugin_name: str, file_id: str, forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None, options: dict = None) -> Any:
		"""
		Returns a list of all the modules valid for the inputs.
		:param plugin_name: The name of the plugin used as a UUID
		:param file_id: The furthest down id in the list. (eg game identifier, forge file name, datafile id or actual file id)
		:param forge_file_name: The name of the forge file
		:param datafile_id: The integer value of the datafile
		:param options: options to be passed to the plugin
		:return:
		"""
		self._load_plugins()

		plugin = self._get_plugin(plugin_name)
		output = plugin.plugin(self.pyUbiForge, file_id, forge_file_name, datafile_id, options)
		# the plugin should return a tuple with the first argument being the specification for the next screen (or None if not applicable)
		# and the second being any optional return data. If only one thing is returned it will be assumed this is the output data
		# (eg the implied `return None` at the end of any function)
		if isinstance(output, tuple) and len(output) == 2:
			return output
		else:
			return None, output

	def _get_plugin(self, plugin_name: str):
		plugin = self.plugin_names.get(plugin_name, None)
		if plugin is None:
			self.pyUbiForge.log.warn(__name__, f'Could not find plugin "{plugin_name}"')
			raise Exception
		return plugin

	def _load_plugins(self):
		"""Call this method to load plugins from disk. (This method is automatically called by the get method)"""
		if self.pyUbiForge.game_identifier != self.game_identifier:
			self.game_identifier = self.pyUbiForge.game_identifier
			self.plugins = {1: {}, 2: {}, 3: {}, 4: {'*': {}}}
			self.plugin_names = {}
			# iterate through every plugin
			for finder, name, _ in pkgutil.iter_modules([f'./pyUbiForge/{self.pyUbiForge.game_identifier}/right_click_methods']):
				# load module and confirm that all required attributes are defined
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

				# The plugin name is used as a UUID so make sure that it is unique
				if module.plugin_name in self.plugin_names:
					self.pyUbiForge.log.warn(__name__, f'Multiple plugins defined with name "{module.plugin_name}"')
					continue
				self.plugin_names[module.plugin_name] = module

				# store the plugin in the relevant location
				if module.plugin_level in [1, 2, 3]:
					self.plugins[module.plugin_level][module.plugin_name] = module
				else:
					if module.file_type not in self.plugins[module.plugin_level]:
						self.plugins[module.plugin_level][module.file_type] = {}
					self.plugins[module.plugin_level][module.file_type][module.plugin_name] = module

				self.pyUbiForge.log.info(__name__, f'Successfully loaded right click plugin: "{module.plugin_name}"')


class DataTypeHandler:
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self.game_identifier = None
		self.plugins = {}

	def __call__(self, file_object_data_wrapper: FileObjectDataWrapper, out_file: Union[None, FileObjectDataWrapper, TextIO] = None, indent_count: int = 0):
		"""
		Call this function in the right click methods as the start point
		Will call get_data_recursive to get the actual data followed by the clever_format method to read the rest of the file
		:param file_object_data_wrapper: The input raw data
		:param out_file: A file object to output the formatted data to
		:param indent_count: The number of indents in out_file
		:return: objects defined in the plugins
		"""
		self._load_plugins()
		if not isinstance(file_object_data_wrapper, FileObjectDataWrapper):
			raise Exception('file_object_data_wrapper is not of type FileObjectDataWrapper')
		file_object_data_wrapper.read_str(self.pyUbiForge.game_functions.pre_header_length, out_file, indent_count)
		try:
			data = self.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		except:
			data = None
		file_object_data_wrapper.clever_format(out_file, indent_count)
		return data

	def get_data_recursive(self, file_object_data_wrapper: FileObjectDataWrapper, out_file: Union[None, FileObjectDataWrapper, TextIO], indent_count: int = 0):
		"""
		Call this function in file reader methods to access other file types in the same file
		:param file_object_data_wrapper: The input raw data
		:param out_file: A file object to output the formatted data to
		:param indent_count: The number of indents in out_file
		:return: objects defined in the plugins
		"""

		file_object_data_wrapper.read_id(out_file, indent_count)
		file_type = file_object_data_wrapper.read_type(out_file, indent_count)
		if file_type in self.plugins:
			return self.plugins[file_type](self.pyUbiForge, file_object_data_wrapper, out_file, indent_count+1)
		else:
			raise Exception(f'File type {file_type} does not have a file reader')

	def _load_plugins(self):
		"""Call this method to load plugins from disk. (This method is automatically called by the get method)"""
		if self.pyUbiForge.game_identifier != self.game_identifier:
			self.game_identifier = self.pyUbiForge.game_identifier
			self.plugins = {}
			for finder, name, _ in pkgutil.iter_modules([f'./pyUbiForge/{self.pyUbiForge.game_identifier}/type_readers']):
				plugin = load_module(name, finder.path)

				if not hasattr(plugin, 'file_type'):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not defined')
					continue
				elif not isinstance(plugin.file_type, str):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not a string')
					continue
				try:
					file_type = plugin.file_type
				except Exception as e:
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because parsing of "file_type" failed\n{e}')
					continue

				if not hasattr(plugin, 'plugin'):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin" was not defined')
					continue

				if file_type in self.plugins:
					self.pyUbiForge.log.warn(__name__, f'Skipping plugin "{name}" because a reader for this file type was already found')
					continue
				else:
					self.plugins[file_type] = plugin.plugin


def load_module(name: str, path: str):
	"""Helper function to load a module"""
	module_spec = importlib.util.spec_from_file_location(name, f'{path}/{name}.py')
	module = importlib.util.module_from_spec(module_spec)
	module_spec.loader.exec_module(module)
	return module
