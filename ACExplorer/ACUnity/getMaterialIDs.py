from ACExplorer.ACUnity.decompressDatafile import decompressDatafile
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import BEHEX2


def getMaterialIDs(fileTree, fileList, fileID):
	if not tempFiles.exists(fileID):
		decompressDatafile(fileTree, fileList, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	fileDir = data['dir']
	materialFile = open(fileDir, 'rb')
	_ = materialFile.read(26)
	materialTemplateID = BEHEX2(materialFile.read(8)).upper()
	materialFile.close()

	if not tempFiles.exists(materialTemplateID):
		decompressDatafile(fileTree, fileList, materialTemplateID)

	try:
		materialTemplate = open(tempFiles.read(materialTemplateID)[0]['dir'], 'rb')
	except:
		return
	textures = {}
	_ = materialTemplate.read(16)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['diffuse'] = idtemp

	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['normal'] = idtemp
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['specular'] = idtemp
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['height'] = idtemp
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception(data['dir'] + ' has an id in position 5') 
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['TransmissionMap'] = idtemp
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception(data['dir'] + ' has an id in position 7') 
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['mask1map'] = idtemp
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['mask2map'] = idtemp
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception(data['dir'] + ' has an id in position 10') 
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception(data['dir'] + ' has an id in position 11') 
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception(data['dir'] + ' has an id in position 12') 
	
	materialTemplate.close()
	
	return textures
