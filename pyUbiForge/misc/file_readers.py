import pkgutil
import importlib
from typing import Union, TextIO
from pyUbiForge.misc.file_object import FileObjectDataWrapper


class FileReaderHandler:
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
