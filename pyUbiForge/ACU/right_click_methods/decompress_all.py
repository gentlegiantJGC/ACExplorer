from pyUbiForge.misc.plugins import BasePlugin


class Plugin(BasePlugin):
	plugin_name = 'Decompress All'
	plugin_level = 1

	def run(self, py_ubi_forge, *_):
		datafile_count = 0
		datafile_completed_count = 0
		for forge_file_name in py_ubi_forge.forge_files:
			datafile_count += len(py_ubi_forge.forge_files[forge_file_name].datafiles)

		for forge_file_name in py_ubi_forge.forge_files:
			for file_id in py_ubi_forge.forge_files[forge_file_name].datafiles:
				try:
					py_ubi_forge.temp_files(file_id, forge_file_name, file_id)
				except:
					continue
				datafile_completed_count += 1
				if datafile_completed_count % 100 == 99:
					py_ubi_forge.log.info(__name__, f"Decompressed {round(100*datafile_completed_count/datafile_count, 2)}% of {datafile_count} datafiles")
		py_ubi_forge.log.info(__name__, "Decompressed all files")
