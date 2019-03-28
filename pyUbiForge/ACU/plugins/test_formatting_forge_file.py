from pyUbiForge.misc.plugins import BasePlugin
from pyUbiForge.misc.file_object import FileObject
from concurrent.futures import ThreadPoolExecutor
import os
from typing import Union, List
import random


def read_file(py_ubi_forge, data, file_id):
	try:
		out_file = FileObject()
		py_ubi_forge.read_file(data.file, out_file)
		out_file.close(
			os.path.join(
				py_ubi_forge.CONFIG.get('dumpFolder', 'output'),
				f'{py_ubi_forge.game_functions.game_identifier}_{data.file_name}_{file_id:016X}.format'
			)
		)
	except Exception as e:
		py_ubi_forge.log.warn(e)


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

	def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: Union[List[dict], None] = None):
		if options is not None:
			self._options = options     # should do some validation here

		file_types = [file_type.upper() for file_type in self._options[0].get("File Types", "").split(';')]

		max_count = self._options[0].get("Format Count", 1000)
		files_done = 0
		datafiles_done = 0
		datafile_count = len(py_ubi_forge.forge_files[forge_file_name].datafiles)
		# executor = ThreadPoolExecutor()
		for datafile_id, datafile in random.sample(
				list(py_ubi_forge.forge_files[forge_file_name].datafiles.items()),
				datafile_count
		):
			try:
				py_ubi_forge.temp_files(datafile_id, forge_file_name, datafile_id)
			except:
				continue
			for file_id in datafile.files.keys():
				data = py_ubi_forge.temp_files(file_id, forge_file_name, datafile_id)
				if data is None:
					py_ubi_forge.log.warn(__name__, f"Failed to find file {file_id:016X}")
					return
				if data.file_type not in file_types:
					continue

				py_ubi_forge.log.info(__name__, data.file_name)
				# executor.submit(read_file, py_ubi_forge, data, file_id)
				read_file(py_ubi_forge, data, file_id)
				files_done += 1
				if files_done >= max_count:
					break
			if files_done >= max_count:
				break
			if datafiles_done % 100 == 99:
				py_ubi_forge.log.info(__name__, f"Processed {round(100*datafiles_done/datafile_count, 2)}% of {datafile_count} datafiles")
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
