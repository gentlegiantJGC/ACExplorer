plugin_name = 'Decompress Forge'
plugin_level = 2


def plugin(py_ubi_forge, forge_file_name, *_):
	datafile_count = len(py_ubi_forge.forge_files[forge_file_name].datafiles)
	count = 0
	for file_id in py_ubi_forge.forge_files[forge_file_name].datafiles:
		try:
			py_ubi_forge.temp_files(file_id, forge_file_name, file_id)
		except:
			continue
		count += 1
		if count % 10000:
			py_ubi_forge.log.info(__name__, f"Decompressed {round(100*count/datafile_count, 2)}% of {datafile_count} datafiles")
	py_ubi_forge.log.info(__name__, "Decompressed all files")
