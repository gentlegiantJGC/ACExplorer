import binascii

from ACExplorer.ACUnity.decompressDatafile import decompressDatafile
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import BEHEX2, float32
from ACExplorer.misc.exportOBJMulti import exportOBJMulti


def exportFakes(fileTree, fileList, fileID):
	if not tempFiles.exists(fileID):
		decompressDatafile(fileTree, fileList, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	
	fIn = open(data['dir'], 'rb')
	fReadIn = fIn.read()
	fIn.close()

	files = fReadIn.split(binascii.unhexlify('000000000000000024B57FD7'))[1:]
	
	fileIDList = []
	for n in files:
		if binascii.unhexlify('298D65EC') not in n:
			continue
		fileContainer = {}
		fileContainer['transformationMtx'] = [[],[],[],[]]
		fileContainer['transformationMtx'][0].append(float32(n[15:19]))
		fileContainer['transformationMtx'][1].append(float32(n[19:23]))
		fileContainer['transformationMtx'][2].append(float32(n[23:27]))
		fileContainer['transformationMtx'][3].append(float32(n[27:31]))
		fileContainer['transformationMtx'][0].append(float32(n[31:35]))
		fileContainer['transformationMtx'][1].append(float32(n[35:39]))
		fileContainer['transformationMtx'][2].append(float32(n[39:43]))
		fileContainer['transformationMtx'][3].append(float32(n[43:47]))
		fileContainer['transformationMtx'][0].append(float32(n[47:51]))
		fileContainer['transformationMtx'][1].append(float32(n[51:55]))
		fileContainer['transformationMtx'][2].append(float32(n[55:59]))
		fileContainer['transformationMtx'][3].append(float32(n[59:63]))
		fileContainer['transformationMtx'][0].append(float32(n[63:67]))
		fileContainer['transformationMtx'][1].append(float32(n[67:71]))
		fileContainer['transformationMtx'][2].append(float32(n[71:75]))
		fileContainer['transformationMtx'][3].append(float32(n[75:79]))
		visualLoc = n.find(binascii.unhexlify('298D65EC'))
		fileContainer['fileID'] = BEHEX2(n[visualLoc+8:visualLoc+16]).upper()
		fileIDList.append(fileContainer)
	
	exportOBJMulti(fileTree, fileList, fileID, fileIDList)
