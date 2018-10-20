from ACExplorer.ACUnity.decompressDatafile_ import decompressDatafile
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import BEHEX2, LE2DEC2, float32
from ACExplorer.misc.exportOBJMulti import exportOBJMulti
from ACExplorer.ACUnity import formatFile
import sys

def mul4x4(A,B):
	C = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for x in range(4):
		for y in range(4):
			for z in range(4):
				C[x][y] += A[x][z]*B[z][y]
	return C

def exportDataBlockModels(app, fileID):
	if not tempFiles.exists(fileID):
		decompressDatafile(app, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file {} is empty'.format(fileID))
	data = data[0]

	if data['fileType'] != 'AC2BBF68':
		return
	
	if 'dev' in sys.argv:
		reload(formatFile)  # for development
	dataBlock = formatFile.topLevelFormat(app, fileID)
	# fileID, data and dataBlock all relate to the DataBlock file (Type AC2BBF68)
	# This is a list of every file called by that DataBlock
	# formatFile.topLevelFormat will return this list of files into dataBlock
	
	fileIDList = {}
	
	for n, fileID2 in enumerate(dataBlock['dataBlock']):
		if not tempFiles.exists(fileID2):
			decompressDatafile(app, fileID2)
		data2 = tempFiles.read(fileID2)
		if len(data2) == 0:
			raise Exception('file {} is empty'.format(fileID2))
		data2 = data2[0]
		
		print 'Reading {}. {} of {}'.format(data2['fileName'], str(n+1), len(dataBlock['dataBlock']))
	
		dataBlockChild = formatFile.topLevelFormat(app, fileID2)
		# fileID2, data2 and dataBlockChild all relate to the files contained in
		# the DataBlock file. The file could be of a number of types including
		# entities and entity groups
		if dataBlockChild['fileType'] == '0984415E': # entity
			if 'fileIDList' in dataBlockChild:
				for fileID3 in dataBlockChild['fileIDList']:
					if not tempFiles.exists(fileID3):
						decompressDatafile(app, fileID3)
					data3 = tempFiles.read(fileID3)
					if len(data3) == 0:
						raise Exception('file {} is empty'.format(fileID3))
					data3 = data3[0]
					if data3['fileType'] == '415D9568':
						if fileID3 not in fileIDList:
							fileIDList[fileID3] = []
						fileIDList[fileID3] += dataBlockChild['fileIDList'][fileID3]
						# fileIDList.append({'fileID':fileID3, 'transformationMtx': dataBlockChild['transformationMtx']})
					else:
						raise Exception(fileID3+' is not a 3D model')
		
		elif dataBlockChild['fileType'] == '1CBDE084':
			if 'files' in dataBlockChild:
				for fileID3 in dataBlockChild['files']:
					if not tempFiles.exists(fileID3):
						decompressDatafile(app, fileID3)
					data3 = tempFiles.read(fileID3)
					if len(data3) == 0:
						continue
						raise Exception('file '+fileID3+' is empty')
					data3 = data3[0]
					
					if data3['fileType'] in ['0984415E','3F742D26']: # entity
						dataBlockChild2 = formatFile.topLevelFormat(app, fileID3)
						if 'fileIDList' in dataBlockChild2:
							for fileID4 in dataBlockChild2['fileIDList']:
								if not tempFiles.exists(fileID4):
									decompressDatafile(app, fileID4)
								data4 = tempFiles.read(fileID4)
								if len(data4) == 0:
									raise Exception('file {} is empty'.format(fileID4))
								data4 = data4[0]
								if data4['fileType'] == '415D9568':
									
									# fileIDList.append({'fileID':fileID4, 'transformationMtx': dataBlockChild2['transformationMtx']})
									if fileID4 not in fileIDList:
										fileIDList[fileID4] = []
									fileIDList[fileID4] += dataBlockChild2['fileIDList'][fileID4]
								else:
									raise Exception(fileID4+' is not a 3D model')
					else:
						raise Exception('found file type {}'.format(data3['fileType']))
		
		else:
			print 'Could not read following file. Unsupported type.'
			print data2['fileName']
			print dataBlockChild['fileType']
			print dataBlockChild['fileID']
	
	# fIn = open(data['dir'], 'rb')
	# fIn.seek(14)

	# count = LE2DEC2(fIn.read(4))
	# fileIDList = {}
	# ticker = 0
	# for n in range(count):
		# fIn.seek(2,1)
		# fileID2 = BEHEX2(fIn.read(8)).upper()
		# if not tempFiles.exists(fileID2):
			# decompressDatafile(app, fileID2)
		# data2 = tempFiles.read(fileID2)
		# if len(data2) == 0:
			# raise Exception('file '+fileID2+' is empty')
		# data2 = data2[0]
		
		# print 'Reading '+data2['fileName']+'. '+str(n+1)+' of '+str(count)

		# if data2['fileType'] == '0984415E':
			# fIn2 = open(data2['dir'], 'rb')
			# fIn2.seek(14)
			# fIn2.seek(49, 1)
			# xpos = float32(fIn2.read(4))
			# ypos = float32(fIn2.read(4))
			# zpos = float32(fIn2.read(4))
			# filePointer = fIn2.tell()
			# tempFile = fIn2.read()
			# meshLoc = tempFile.find('\x3B\x96\x6E\x53')
			# if meshLoc == -1:
				# continue
			# fIn2.seek(filePointer)
			# fIn2.seek(meshLoc+5, 1)
			# fileID3 = BEHEX2(fIn2.read(8)).upper()
			# if not tempFiles.exists(fileID3):
				# decompressDatafile(app, fileID3)
			# data3 = tempFiles.read(fileID3)
			# if len(data3) == 0:
				# raise Exception('file '+fileID3+' is empty')
			# data3 = data3[0]
			# if data3['fileType'] == '415D9568':
				# fileIDList[ticker] = {'id':fileID3, 'x':xpos, 'y':ypos, 'z':zpos}
				# ticker += 1
			# else:
				# raise Exception(fileID3+' is not a 3D model')
				
	print 'done reading'
	print 'exporting'

	exportOBJMulti(app, fileID, fileIDList)
	
	# print 'Done'
