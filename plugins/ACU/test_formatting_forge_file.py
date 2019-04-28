from plugins import BasePlugin
from pyUbiForge.misc.file_object import FileObject
import os
from typing import Union, List
import random
import pyUbiForge
import logging


def read_file(data, file_id):
	try:
		out_file = FileObject()
		pyUbiForge.read_file(data.file, out_file)
		out_file.close(
			os.path.join(
				pyUbiForge.CONFIG.get('dumpFolder', 'output'),
				f'{pyUbiForge.game_identifier()}_{data.file_name}_{file_id:016X}.format'
			)
		)
	except Exception as e:
		logging.warning(e)


class Plugin(BasePlugin):
	plugin_name = 'Test Formatting Forge File'
	plugin_level = 2
	dev = True
	_options = [
		{
			"File Types": "0984415E;85C817C3",
			"Format Count": 1000
		}
	]

	def run(self, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: Union[List[dict], None] = None):
		if options is not None:
			self._options = options     # should do some validation here

		file_types = [file_type.upper() for file_type in self._options[0].get("File Types", "").split(';')]

		max_count = self._options[0].get("Format Count", 1000)
		files_done = 0
		datafiles_done = 0
		datafile_count = len(pyUbiForge.forge_files[forge_file_name].datafiles)
		# executor = ThreadPoolExecutor()
		for datafile_id, datafile in random.sample(
				list(pyUbiForge.forge_files[forge_file_name].datafiles.items()),
				datafile_count
		):
			try:
				pyUbiForge.temp_files(datafile_id, forge_file_name, datafile_id)
			except:
				continue
			for file_id in datafile.files.keys():
				data = pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)
				if data is None:
					logging.warning(f"Failed to find file {file_id:016X}")
					return
				if data.file_type not in file_types:
					continue

				logging.info(data.file_name)
				# executor.submit(read_file, pyUbiForge, data, file_id)
				read_file(pyUbiForge, data, file_id)
				files_done += 1
				if files_done >= max_count:
					break
			if files_done >= max_count:
				break
			if datafiles_done % 100 == 99:
				logging.info(f"Processed {round(100*datafiles_done/datafile_count, 2)}% of {datafile_count} datafiles")
			datafiles_done += 1

	def options(self, options: Union[List[dict], None]):
		if options is None or (isinstance(options, list) and len(options) == 0):
			return {
				"File Types": {
					"type": "str_entry",
					"default": self._options[0]["File Types"]
				},
				"Format Count": {
					"type": "int_entry",
					"default": self._options[0]["Format Count"],
					"min": 0
				}
			}
		else:
			self._options = options
