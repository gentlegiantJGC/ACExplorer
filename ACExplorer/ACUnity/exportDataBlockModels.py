from ACExplorer.ACUnity.decompressDatafile import decompressDatafile
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import BEHEX2, LE2DEC2, float32
from ACExplorer.misc.exportOBJMulti import exportOBJMulti


def exportDataBlockModels(fileTree, fileList, fileID):
	if not tempFiles.exists(fileID):
		decompressDatafile(fileTree, fileList, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]

	if data['resourceType'] != 'AC2BBF68':
		return
	
	fIn = open(data['dir'], 'rb')
	fIn.seek(14)

	count = LE2DEC2(fIn.read(4))
	fileIDList = {}
	ticker = 0
	for n in range(count):
		fIn.seek(2,1)
		fileID2 = BEHEX2(fIn.read(8)).upper()
		# print str(fileID2) + '\t\t' + tempFiles[fileID2]['fileName']
		# print tempFiles[fileID2]['resourceType']
		if not tempFiles.exists(fileID2):
			decompressDatafile(fileTree, fileList, fileID2)
		data2 = tempFiles.read(fileID2)
		if len(data2) == 0:
			raise Exception('file '+fileID2+' is empty')
		data2 = data2[0]
		
		print 'Reading '+data2['fileName']+'. '+str(n+1)+' of '+str(count)

		if data2['resourceType'] == '0984415E':
			fIn2 = open(data2['dir'], 'rb')
			fIn2.seek(14)
			fIn2.seek(49, 1)
			xpos = float32(fIn2.read(4))
			ypos = float32(fIn2.read(4))
			zpos = float32(fIn2.read(4))
			filePointer = fIn2.tell()
			tempFile = fIn2.read()
			meshLoc = tempFile.find('\x3B\x96\x6E\x53')
			if meshLoc == -1:
				continue
			fIn2.seek(filePointer)
			fIn2.seek(meshLoc+5, 1)
			fileID3 = BEHEX2(fIn2.read(8)).upper()
			if not tempFiles.exists(fileID3):
				decompressDatafile(fileTree, fileList, fileID3)
			data3 = tempFiles.read(fileID3)
			if len(data3) == 0:
				raise Exception('file '+fileID3+' is empty')
			data3 = data3[0]
			if data3['resourceType'] == '415D9568':
				fileIDList[ticker] = {'id':fileID3, 'x':xpos, 'y':ypos, 'z':zpos}
				ticker += 1
			else:
				raise Exception(fileID3+' is not a 3D model')
				
	print 'done reading'
	print 'exporting'

	exportOBJMulti(fileTree, fileList, fileID, fileIDList)
	
	print 'Done'
	
	# import struct
	# struct.unpack('>f',binascii.unhexlify('41406fed'))
