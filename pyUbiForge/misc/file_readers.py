import logging
import pkgutil
import importlib
from typing import Union, TextIO
from pyUbiForge.misc.file_object import FileObjectDataWrapper
import pyUbiForge
import time


class BaseReader:
	file_id: int = None
	file_type: str = None


class FileReaderHandler:
	def __init__(self):
		self.game_identifier = None
		self.readers = {}
		self._time = 0
		self._wait = True

	def __call__(self, file_object_data_wrapper: FileObjectDataWrapper, out_file: Union[None, FileObjectDataWrapper, TextIO] = None):
		"""
		Call this function in the right click methods as the start point
		Will call get_data_recursive to get the actual data followed by the clever_format method to read the rest of the file
		:param file_object_data_wrapper: The input raw data
		:return: objects defined in the plugins
		"""
		file_object_data_wrapper.bind_out_file(out_file)
		self._load_readers()
		while self._wait:
			time.sleep(0.1)
		self._time = time.time()
		if not isinstance(file_object_data_wrapper, FileObjectDataWrapper):
			raise Exception('file_object_data_wrapper is not of type FileObjectDataWrapper')
		file_object_data_wrapper.read_bytes(pyUbiForge.game_functions.pre_header_length)
		try:
			data = self.get_data_recursive(file_object_data_wrapper)
		except Exception as e:
			logging.warning(str(e))
			data = None
		file_object_data_wrapper.clever_format()
		return data

	def get_data_recursive(self, file_object_data_wrapper: FileObjectDataWrapper):
		"""
		Call this function in file reader methods to access other file types in the same file
		:param file_object_data_wrapper: The input raw data
		:return: objects defined in the plugins
		"""

		file_object_data_wrapper.out_file_write('\n')
		file_id = file_object_data_wrapper.read_id()
		file_type = file_object_data_wrapper.read_type()
		if file_type in self.readers:
			file_object_data_wrapper.indent()
			ret = self.readers[file_type](file_object_data_wrapper)
			ret.file_id = file_id
			file_object_data_wrapper.indent(-1)
			return ret
		else:
			raise Exception(f'File type {file_type} does not have a file reader')

	def _load_readers(self):
		"""Call this method to load plugins from disk. (This method is automatically called by the get method)"""
		if (pyUbiForge.game_identifier() != self.game_identifier or pyUbiForge.CONFIG.get('dev', False)) and time.time() > self._time + 10:
			self._time = time.time()
			self._wait = True
			self.game_identifier = pyUbiForge.game_identifier()
			self.readers = {}
			for _, name, _ in pkgutil.iter_modules([f'./pyUbiForge/{pyUbiForge.game_identifier()}/type_readers']):
				module = importlib.import_module(f'pyUbiForge.{pyUbiForge.game_identifier()}.type_readers.{name}')
				importlib.reload(module)

				if not hasattr(module, 'Reader') and issubclass(module.Reader, BaseReader):
					logging.warning(f'Failed loading {name} because "Reader" was either not defined, not a class or not a subclass of BaseReader')
					continue

				reader = module.Reader

				if not hasattr(reader, 'file_type'):
					logging.warning(f'Failed loading {name} because "file_type" was not defined')
					continue
				elif not isinstance(reader.file_type, str):
					logging.warning(f'Failed loading {name} because "file_type" was not a string')
					continue

				file_type = reader.file_type

				if file_type in self.readers:
					logging.warning(f'Skipping plugin "{name}" because a reader for this file type was already found')
					continue
				else:
					self.readers[file_type] = reader
			self._wait = False


file_reader_handler = FileReaderHandler()
