plugin_name = 'Decompress All'
plugin_level = 2


def plugin(py_ubi_forge, forge_file_name, *_):
	for file_id in py_ubi_forge.file_list[forge_file_name]:
		py_ubi_forge.temp_files(file_id, forge_file_name, file_id)
