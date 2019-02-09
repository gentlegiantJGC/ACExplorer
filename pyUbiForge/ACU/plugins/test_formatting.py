from pyUbiForge.misc.plugins import BasePlugin
import os


class Plugin(BasePlugin):
	plugin_name = 'Test Formatting'
	plugin_level = 3
	dev = True

	def run(self, py_ubi_forge, file_id, forge_file_name, datafile_id, options):
		for file_id in py_ubi_forge.forge_files[forge_file_name].datafiles[datafile_id].files.keys():
			data = py_ubi_forge.temp_files(file_id, forge_file_name, datafile_id)
			if data is None:
				py_ubi_forge.log.warn(__name__, f"Failed to find file {file_id:016X}")
				return
			if data.file_type not in ['0984415E']:
				continue

			output = py_ubi_forge.read_file(data.file)

			if output is None:
				py_ubi_forge.log.warn(__name__, data.file_name)
				out_file = open(
					os.path.join(
						py_ubi_forge.CONFIG['dumpFolder'],
						f'{py_ubi_forge.game_functions.game_identifier}_{data.file_name}_{file_id:016X}.format'
					), 'w'
				)
				py_ubi_forge.read_file(data.file, out_file)
