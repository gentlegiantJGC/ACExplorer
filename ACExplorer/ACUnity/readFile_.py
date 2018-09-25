import sys


def readFile(app, fileID, forgeFile=None, datafileID=None):
	data = app.tempNewFiles.getData(fileID, forgeFile, datafileID)
	if data is None:
		raise Exception('issue getting file "{}"'.format(fileID))
	
	if data['resourceType'] == '415D9568':	#mesh (textures looked up)
		return #TODO make this work with the new system
		app.log.info(__name__, 'Exporting '.format(data['fileName']))
		app.gameFunctions.readModel(app, fileID)
		app.gameFunctions.exportOBJ(app, fileID)
	elif data['resourceType'] == 'AC2BBF68': #datablock (includes world data)
		app.gameFunctions.exportDataBlockModels(app, fileID)
	elif data['resourceType'] == 'A2B7E917': #texture
		app.gameFunctions.exportTexture(app, fileID)
	elif data['resourceType'] == '85C817C3': #material (containing textures)
		textureIDs = app.gameFunctions.getMaterialIDs(app, fileID)
		if textureIDs == None:
			return
		else:
			for hexid in textureIDs:
				app.gameFunctions.exportTexture(app, textureIDs[hexid])
	elif data['resourceType'] =='C69A7F31':	#fakes
		app.gameFunctions.exportFakes(app, fileID)
	else:
		if 'dev' in sys.argv:
			reload(app.gameFunctions.formatFile)  # for development
		app.gameFunctions.formatFile.topLevelFormat(app, fileID)
