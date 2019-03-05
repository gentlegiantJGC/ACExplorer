import pkgutil
import importlib
from typing import Tuple, Union, Any


class BasePlugin:
	plugin_name = None
	plugin_level = None
	file_type = None
	dev = False

	def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: list):
		pass


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
	>>>		def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: list):
	>>>			# the method that is called to run the plugin
	>>>			if options is None:
	>>>				# if the script requires inputs then populate options with the default options
	>>>             self.script_options = __script_options__
	>>>			elif options == []:  # This is the normal first input
	>>>				# if the script requires options then return the specification for the first screen
	>>>             return __new_screen_options__, None
	>>>             # the first return value must be the next screen or None if there are no more screens.
	>>>             # The second is the normal return value which can be whatever you want
	>>>         # options will be a list containing a dictionary for each of the screens completed.
	>>>         # Do what you need to and return a new screen for any new data the script needs
	>>>         # When you no longer need any more inputs run the actual script
	>>>         # Finally return the below. Make sure the first value is None otherwise it will get stuck in an infinate loop. __return_value__ can be None
	>>>         return None, __return_value__



	plugin_level = integer 1, 2, 3 or 4  # this is the level in the file tree this plugin applies to.
		1 - the top entry
		2 - the forge file
		3 - the datafile (for plugins specific to a certain file type use 4, those will appear here as well)
		4 - the specific file in the datafile and the parent datafile with the same id
			if plugin_level == 4 then the big endian hex string representation of the file type must be given
			file_type = '415D9568'
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
		output = plugin.run(self.pyUbiForge, file_id, forge_file_name, datafile_id, options)
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
		if self.pyUbiForge.game_identifier != self.game_identifier or self.pyUbiForge.CONFIG.get('dev', False):
			self.game_identifier = self.pyUbiForge.game_identifier
			self.plugins = {1: {}, 2: {}, 3: {}, 4: {'*': {}}}
			self.plugin_names = {}
			# iterate through every plugin
			for _, name, _ in pkgutil.iter_modules([f'./pyUbiForge/{self.pyUbiForge.game_identifier}/plugins']):
				# load module and confirm that all required attributes are defined
				module = importlib.import_module(f'pyUbiForge.{self.pyUbiForge.game_identifier}.plugins.{name}')
				importlib.reload(module)

				if not hasattr(module, 'Plugin') and issubclass(module.Plugin, BasePlugin):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "Plugin" was either not defined, not a class or not a subclass of BasePlugin')
					continue

				plugin = module.Plugin

				if not isinstance(plugin.dev, bool):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "Plugin.dev" was not a bool')
					continue
				else:
					if plugin.dev and not self.pyUbiForge.CONFIG.get('dev', False):
						continue

				if not isinstance(plugin.plugin_name, str):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "Plugin.plugin_name" was not a string')
					continue
				if not isinstance(plugin.plugin_level, int) and plugin.plugin_level in [1, 2, 3, 4]:
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "plugin_level" was not an int in [1,2,3,4]')
					continue
				if plugin.plugin_level == 4:
					if not isinstance(plugin.file_type, str):
						self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not defined or was not a string')
						continue

				# The plugin name is used as a UUID so make sure that it is unique
				if plugin.plugin_name in self.plugin_names:
					self.pyUbiForge.log.warn(__name__, f'Multiple plugins defined with name "{plugin.plugin_name}"')
					continue

				plugin_instance = plugin()

				self.plugin_names[plugin.plugin_name] = plugin_instance

				# store the plugin in the relevant location
				if plugin.plugin_level in [1, 2, 3]:
					self.plugins[plugin.plugin_level][plugin.plugin_name] = plugin_instance
				else:
					if plugin.file_type not in self.plugins[plugin.plugin_level]:
						self.plugins[plugin.plugin_level][plugin.file_type] = {}
					self.plugins[plugin.plugin_level][plugin.file_type][plugin.plugin_name] = plugin_instance
