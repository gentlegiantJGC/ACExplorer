plugin_name = 'Export DDS'
plugin_level = 4
file_type = 'A2B7E917'


def plugin(app, file_id, forge_file_name, datafile_id):
	# TODO add select directory option
	save_folder = app.CONFIG['dumpFolder']
	app.misc.texture.export_dds(app, file_id, forge_file_name, datafile_id, save_folder)
