from plugins import BasePlugin
import pyUbiForge
import logging


class Plugin(BasePlugin):
	plugin_name = 'Decompress All'
	plugin_level = 1

	def run(self, *_):
		datafile_count = 0
		datafile_completed_count = 0
		for forge_file_name in pyUbiForge.forge_files:
			datafile_count += len(pyUbiForge.forge_files[forge_file_name].datafiles)

		for forge_file_name in pyUbiForge.forge_files:
			for file_id in pyUbiForge.forge_files[forge_file_name].datafiles:
				try:
					pyUbiForge.temp_files(file_id, forge_file_name, file_id)
				except:
					continue
				datafile_completed_count += 1
				if datafile_completed_count % 100 == 99:
					logging.info(f"Decompressed {round(100*datafile_completed_count/datafile_count, 2)}% of {datafile_count} datafiles")
		logging.info("Decompressed all files")
