def readFile(fileTree, fileList, config, fileID):
	from ACUnity.decompressDatafile import decompressDatafile
	from ACUnity.exportTexture import exportTexture
	
	from misc import tempFiles
	
	# fileID = fileID.upper()
	if not tempFiles.exists(config, fileID):
		decompressDatafile(fileTree, fileList, config, fileID)
	data = tempFiles.read(config, fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	
	if data['resourceType'] == '415D9568':	#mesh (textures looked up)
		print 'Exporting '+data['fileName']
		from ACUnity.readModel import readModel
		from misc.exportOBJ import exportOBJ
		readModel(fileTree, fileList, config, fileID)
		exportOBJ(fileTree, fileList, config, fileID)
	elif data['resourceType'] == 'AC2BBF68': #datablock (includes world data)
		from ACUnity.exportDataBlockModels import exportDataBlockModels
		exportDataBlockModels(fileTree, fileList, config, fileID)
	elif data['resourceType'] == 'A2B7E917': #texture
		exportTexture(fileTree, fileList, config, fileID)
	elif data['resourceType'] == '85C817C3': #material (containing textures)
		from ACUnity.getMaterialIDs import getMaterialIDs
		textureIDs = getMaterialIDs(fileTree, fileList, config, fileID)
		if textureIDs == None:
			return
		else:
			for hexid in textureIDs:
				exportTexture(fileTree, fileList, config, textureIDs[hexid])
	elif data['resourceType'] =='C69A7F31':	#fakes
		from ACUnity.exportFakes import exportFakes
		exportFakes(fileTree, fileList, config, fileID)
	else:
		from ACUnity import format
		reload(format)
		format.format(fileTree, fileList, config, fileID)