import pkgutil
import importlib
from typing import Union, TextIO
from pyUbiForge.misc.file_object import FileObjectDataWrapper


class BaseReader:
	file_type = None


class FileReaderHandler:
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self.game_identifier = None
		self.readers = {}

	def __call__(self, file_object_data_wrapper: FileObjectDataWrapper, out_file: Union[None, FileObjectDataWrapper, TextIO] = None, indent_count: int = 0):
		"""
		Call this function in the right click methods as the start point
		Will call get_data_recursive to get the actual data followed by the clever_format method to read the rest of the file
		:param file_object_data_wrapper: The input raw data
		:param out_file: A file object to output the formatted data to
		:param indent_count: The number of indents in out_file
		:return: objects defined in the plugins
		"""
		self._load_readers()
		if not isinstance(file_object_data_wrapper, FileObjectDataWrapper):
			raise Exception('file_object_data_wrapper is not of type FileObjectDataWrapper')
		file_object_data_wrapper.read_str(self.pyUbiForge.game_functions.pre_header_length, out_file, indent_count)
		try:
			data = self.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		except Exception as e:
			self.pyUbiForge.log.warn(__name__, e)
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

		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		file_object_data_wrapper.read_id(out_file, indent_count)
		file_type = file_object_data_wrapper.read_type(out_file, indent_count)
		if file_type in self.readers:
			return self.readers[file_type](self.pyUbiForge, file_object_data_wrapper, out_file, indent_count + 1)
		else:
			raise Exception(f'File type {file_type} does not have a file reader')

	def _load_readers(self):
		"""Call this method to load plugins from disk. (This method is automatically called by the get method)"""
		if self.pyUbiForge.game_identifier != self.game_identifier or self.pyUbiForge.CONFIG.get('dev', False):
			self.game_identifier = self.pyUbiForge.game_identifier
			self.readers = {}
			for _, name, _ in pkgutil.iter_modules([f'./pyUbiForge/{self.pyUbiForge.game_identifier}/type_readers']):
				module = importlib.import_module(f'pyUbiForge.{self.pyUbiForge.game_identifier}.type_readers.{name}')
				importlib.reload(module)

				if not hasattr(module, 'Reader') and issubclass(module.Reader, BaseReader):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "Reader" was either not defined, not a class or not a subclass of BaseReader')
					continue

				reader = module.Reader

				if not hasattr(reader, 'file_type'):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not defined')
					continue
				elif not isinstance(reader.file_type, str):
					self.pyUbiForge.log.warn(__name__, f'Failed loading {name} because "file_type" was not a string')
					continue

				file_type = reader.file_type

				if file_type in self.readers:
					self.pyUbiForge.log.warn(__name__, f'Skipping plugin "{name}" because a reader for this file type was already found')
					continue
				else:
					self.readers[file_type] = reader
