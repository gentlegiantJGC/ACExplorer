from ACExplorer.ACUnity.decompressDatafile_ import decompressDatafile
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import BEHEX2


def getMaterialIDs(app, fileID):
	if not tempFiles.exists(fileID):
		decompressDatafile(app, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file {} is empty'.format(fileID))
	data = data[0]
	fileDir = data['dir']
	materialFile = open(fileDir, 'rb')
	_ = materialFile.read(26)
	materialTemplateID = BEHEX2(materialFile.read(8)).upper()
	materialFile.close()

	if not tempFiles.exists(materialTemplateID):
		decompressDatafile(app, materialTemplateID)

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
		raise Exception('{} has an id in position 5'.format(data['dir']))
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		textures['TransmissionMap'] = idtemp
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception('{} has an id in position 7'.format(data['dir']))
	
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
		raise Exception('{} has an id in position 10'.format(data['dir']))
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception('{} has an id in position 11'.format(data['dir']))
	
	_ = materialTemplate.read(2)
	idtemp = BEHEX2(materialTemplate.read(8)).upper()
	if idtemp != '0000000000000000':
		raise Exception('{} has an id in position 12'.format(data['dir']))
	
	materialTemplate.close()
	
	return textures
