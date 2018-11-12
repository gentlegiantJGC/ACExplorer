plugin_name = 'Export OBJ'
plugin_level = 4
file_type = '415D9568'


def plugin(app, file_id):
	# TODO add select directory option
	save_folder = app.CONFIG['dumpFolder']

	data = app.tempNewFiles(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return
	model_name = data['fileName']

	model = app.read_file(data["rawFile"])
	if model is not None:
		obj_handler = app.misc.mesh.ObjMtl(app, model_name, save_folder)
		obj_handler.export(model, model_name)
		obj_handler.save_and_close()
		app.log.info(__name__, 'Exported {:016X}'.format(file_id))
	else:
		app.log.warn(__name__, 'Failed to export {:016X}'.format(file_id))
