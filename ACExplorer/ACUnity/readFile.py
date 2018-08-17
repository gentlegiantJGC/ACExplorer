import sys
from ACExplorer.ACUnity import formatFile
from ACExplorer.ACUnity.decompressDatafile import decompressDatafile
from ACExplorer.ACUnity.exportDataBlockModels import exportDataBlockModels
from ACExplorer.ACUnity.exportFakes import exportFakes
from ACExplorer.ACUnity.exportTexture import exportTexture
from ACExplorer.ACUnity.getMaterialIDs import getMaterialIDs
from ACExplorer.ACUnity.readModel import readModel
from ACExplorer.misc import tempFiles, log
from ACExplorer.misc.exportOBJ import exportOBJ


def readFile(fileTree, fileList, fileID):
	# fileID = fileID.upper()
	if not tempFiles.exists(fileID):
		decompressDatafile(fileTree, fileList, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file {} is empty'.format(fileID))
	data = data[0]
	
	if data['resourceType'] == '415D9568':	#mesh (textures looked up)
		log.info(__name__, 'Exporting '.format(data['fileName']))
		readModel(fileTree, fileList, fileID)
		exportOBJ(fileTree, fileList, fileID)
	elif data['resourceType'] == 'AC2BBF68': #datablock (includes world data)
		exportDataBlockModels(fileTree, fileList, fileID)
	elif data['resourceType'] == 'A2B7E917': #texture
		exportTexture(fileTree, fileList, fileID)
	elif data['resourceType'] == '85C817C3': #material (containing textures)
		textureIDs = getMaterialIDs(fileTree, fileList, fileID)
		if textureIDs == None:
			return
		else:
			for hexid in textureIDs:
				exportTexture(fileTree, fileList, textureIDs[hexid])
	elif data['resourceType'] =='C69A7F31':	#fakes
		exportFakes(fileTree, fileList, fileID)
	else:
		if 'dev' in sys.argv:
			reload(formatFile)  # for development
		formatFile.topLevelFormat(fileTree, fileList, fileID)
