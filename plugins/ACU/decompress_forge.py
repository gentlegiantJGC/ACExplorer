from pyUbiForge.misc.plugins import BasePlugin
import pyUbiForge
import logging


class Plugin(BasePlugin):
	plugin_name = 'Decompress Forge'
	plugin_level = 2

	def run(self, forge_file_name, *_):
		datafile_count = len(pyUbiForge.forge_files[forge_file_name].datafiles)
		count = 0
		for file_id in pyUbiForge.forge_files[forge_file_name].datafiles:
			try:
				pyUbiForge.temp_files(file_id, forge_file_name, file_id)
			except:
				continue
			count += 1
			if count % 100 == 99:
				logging.info(f"Decompressed {round(100*count/datafile_count, 2)}% of {datafile_count} datafiles")
		logging.info("Decompressed all files")
