def export_obj(app, file_id):
	data = app.tempNewFiles.get_data(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return
	model_name = data['fileName']

	model = app.gameFunctions.read_model(app, file_id)
	if model is not None:
		obj_handler = app.misc.mesh.ObjMtl(app, model_name)
		obj_handler.export(model)
		obj_handler.save_and_close()
		app.log.info(__name__, 'Exported {:016X}'.format(file_id))
	else:
		app.log.warn(__name__, 'Failed to export {:016X}'.format(file_id))
