def export_obj(app, file_id):
	data = app.tempNewFiles.getData(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return
	model_name = data['fileName']

	obj_handler = app.misc.mesh.ObjMtl(app, model_name)
	model = app.gameFunctions.read_model(app, file_id)
	obj_handler.export(model)
	obj_handler.save_and_close()