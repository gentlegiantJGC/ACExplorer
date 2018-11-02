def read_file(app, file_id, forge_file_name=None, datafile_id=None):
	data = app.tempNewFiles.getData(file_id, forge_file_name, datafile_id)
	if data is None:
		raise Exception('issue getting file "{:016X}"'.format(file_id))
	
	if data['fileType'] == '415D9568':	 # mesh (textures looked up)
		app.log.info(__name__, 'Exporting '.format(data['fileName']))
		app.gameFunctions.export_obj(app, file_id)
	elif data['fileType'] == 'AC2BBF68':  # datablock (includes world data)
		app.gameFunctions.exportDataBlockModels(app, file_id)
	elif data['fileType'] == 'A2B7E917':  # texture
		app.gameFunctions.export_texture(app, file_id)
	elif data['fileType'] == '85C817C3':  # material (containing textures)
		texture_ids = app.gameFunctions.get_material_ids(app, file_id)
		if texture_ids is None:
			return
		else:
			for hexid in texture_ids:
				app.gameFunctions.export_texture(app, texture_ids[hexid])
	elif data['fileType'] == 'C69A7F31':  # fakes
		app.gameFunctions.export_fakes(app, file_id)
	else:
		if app.dev:
			reload(app.gameFunctions.formatFile)  # for development
		app.gameFunctions.formatFile.topLevelFormat(app, file_id)
