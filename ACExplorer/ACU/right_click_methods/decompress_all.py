plugin_name = 'Decompress All'
plugin_level = 2


def plugin(app, forge_file_name, *_):
	for file_id in app.file_list[forge_file_name]:
		app.tempNewFiles(file_id, forge_file_name, file_id)
