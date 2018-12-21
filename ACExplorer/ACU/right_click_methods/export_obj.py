from ACExplorer.misc import mesh

plugin_name = 'Export OBJ'
plugin_level = 4
file_type = '415D9568'


def plugin(app, file_id, forge_file_name, datafile_id):
	# TODO add select directory option
	save_folder = app.CONFIG['dumpFolder']

	data = app.temp_files(file_id, forge_file_name, datafile_id)
	if data is None:
		app.log.warn(__name__, f"Failed to find file {file_id:016X}")
		return
	model_name = data['fileName']

	model = app.read_file(data["rawFile"])
	if model is not None:
		obj_handler = mesh.ObjMtl(app, model_name, save_folder)
		obj_handler.export(model, model_name)
		obj_handler.save_and_close()
		app.log.info(__name__, f'Exported {file_id:016X}')
	else:
		app.log.warn(__name__, f'Failed to export {file_id:016X}')
