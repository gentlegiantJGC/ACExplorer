import pkgutil
import importlib
from typing import Tuple, List, Union, Any


class BasePlugin:
	plugin_name = None
	plugin_level = None
	file_type = None
	dev = False

	def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: list = None):
		raise NotImplemented

	def options(self, options: Union[List[dict], None]):
		return


class PluginHandler:
	"""
	A class which loads and handles all the plugins.

	The following is a template for a plugin for it to be loaded.
	from pyUbiForge.misc.plugins import BasePlugin

	>>>	class Plugin(BasePlugin):
	>>>		plugin_name = 'Plugin Name' # the name shown to the user an used as a UUID
	>>>		plugin_level = 4            # see plugin_level below
	>>>		file_type = '00000000'      # big endian hex representation of the file type (only needed if plugin_level == 4)
	>>>
	>>>		def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: list = None):
	>>>			# the method that is called to run the plugin
	>>>
	>>>     def options(self, options: Union[List[dict], None]):
	>>>         # return data in the specified format which the wrapper program can show in the UI

	plugin_level = integer 1, 2, 3 or 4  # this is the level in the file tree this plugin applies to.
		1 - the top entry
		2 - the forge file
		3 - the datafile (for plugins specific to a certain file type use 4, those will appear here as well)
		4 - the specific file in the datafile and the parent datafile with the same id
			if plugin_level == 4 then the big endian hex string representation of the file type must be given
			file_type = '415D9568'

	Options: The options function should return a dictionary for the next screen in the following format.
	If there are no more screens to display (or none at all) return None
		{
			"<Option Name>": {
				{
					"type": "select",
					"options": [
						"<option 1>",
						"<option 2>",
						...
					]
				}
			},
			"<Option Name>": {
				{
					"type": "str_entry",
					"default": "<default_entry>"
				}
			},
			"<Option Name>": {
				{
					"type": "int_entry",
					"default": 0
				}
			},
			"<Option Name>": {
				{
					"type": "dir_select"
				}
			},
			"<Option Name>": {
				{
					"type": "file_select"
				}
			}
		}

	The value of options given to the options function will be a list of all the options given in the previous screens.
	For run it will be the result of all the screens.
	(Note the format does allow for a variable number of screens and varying screens based on previous inputs. This is intended)
	"""
	def __init__(self, py_ubi_forge):
		self._pyUbiForge = py_ubi_forge
		self._game_identifier = None
		self._plugins = {1: {}, 2: {}, 3: {}, 4: {'*': {}}}
		self._plugin_names = {}
		"""
		self._plugins = {
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

	def query(self, plugin_level: int, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None) -> Tuple[list, Union[str, int]]:
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
				self._plugins[plugin_level].keys()
			), file_id

		elif plugin_level in (3, 4):
			file_id = int(file_id)
			file_type = self._pyUbiForge.temp_files(file_id, forge_file_name, datafile_id).file_type

			if plugin_level == 3:
				return list(set(
					list(self._plugins[3].keys()) + list(self._plugins[4].get(file_type, {}).keys()) + list(self._plugins[4]['*'].keys())
				)), file_id

			elif plugin_level == 4:
				return list(set(
					list(self._plugins[4].get(file_type, {}).keys()) + list(self._plugins[4]['*'].keys())
				)), file_id

	def run(self, plugin_name: str, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None, options: list = None) -> Tuple[Union[None, dict], Any]:
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

		return plugin.run(self._pyUbiForge, file_id, forge_file_name, datafile_id, options)
		# the plugin should return a tuple with the first argument being the specification for the next screen (or None if not applicable)
		# and the second being any optional return data. If only one thing is returned it will be assumed this is the output data
		# (eg the implied `return None` at the end of any function)
		# if isinstance(output, tuple) and len(output) == 2:
		# 	return output
		# else:
		# 	return None, output

	def options(self, plugin_name: str, options):
		return

	def _get_plugin(self, plugin_name: str):
		plugin = self._plugin_names.get(plugin_name, None)
		if plugin is None:
			self._pyUbiForge.log.warn(__name__, f'Could not find plugin "{plugin_name}"')
			raise Exception
		return plugin

	def _load_plugins(self):
		"""Call this method to load plugins from disk. (This method is automatically called by the get method)"""
		if self._pyUbiForge.game_identifier != self._game_identifier or self._pyUbiForge.CONFIG.get('dev', False):
			self._game_identifier = self._pyUbiForge.game_identifier
			self._plugins = {1: {}, 2: {}, 3: {}, 4: {'*': {}}}
			self._plugin_names = {}
			# iterate through every plugin
			for _, name, _ in pkgutil.iter_modules([f'./pyUbiForge/{self._pyUbiForge.game_identifier}/plugins']):
				# load module and confirm that all required attributes are defined
				module = importlib.import_module(f'pyUbiForge.{self._pyUbiForge.game_identifier}.plugins.{name}')
				importlib.reload(module)

				if not hasattr(module, 'Plugin') and issubclass(module.Plugin, BasePlugin):
					self._pyUbiForge.log.warn(__name__, f'Failed loading {name} because "Plugin" was either not defined, not a class or not a subclass of BasePlugin')
					continue

				plugin = module.Plugin

				if not isinstance(plugin.dev, bool):
					self._pyUbiForge.log.warn(__name__, f'Failed loading {name} because "Plugin.dev" was not a bool')
					continue
				else:
					if plugin.dev and not self._pyUbiForge.CONFIG.get('dev', False):
						continue

				if not isinstance(plugin.plugin_name, str):
					self._pyUbiForge.log.warn(__name__, f'Failed loading {name} because "Plugin.plugin_name" was not a string')
					continue
				if not isinstance(plugin.plugin_level, int) and plugin.plugin_level in [1, 2, 3, 4]:
					self._pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin_level" was not an int in [1,2,3,4]')
					continue
				if plugin.plugin_level == 4:
					if not isinstance(plugin.file_type, str):
						self._pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not defined or was not a string')
						continue

				# The plugin name is used as a UUID so make sure that it is unique
				if plugin.plugin_name in self._plugin_names:
					self._pyUbiForge.log.warn(__name__, f'Multiple plugins defined with name "{plugin.plugin_name}"')
					continue

				plugin_instance = plugin()

				self._plugin_names[plugin.plugin_name] = plugin_instance

				# store the plugin in the relevant location
				if plugin.plugin_level in [1, 2, 3]:
					self._plugins[plugin.plugin_level][plugin.plugin_name] = plugin_instance
				else:
					if plugin.file_type not in self._plugins[plugin.plugin_level]:
						self._plugins[plugin.plugin_level][plugin.file_type] = {}
					self._plugins[plugin.plugin_level][plugin.file_type][plugin.plugin_name] = plugin_instance
