import binascii
import os
import sys
import json
import time
import struct
# from ACExplorer.misc.dataTypes import LE2BE2, BEHEX2, LE2DEC2, int16, uint16, int32, uint32, float32
fileTypes = json.load(open(r"./ACExplorer/ACU/fileFormats.json"))
indentCharacter = '\t'

'''
This module works by calling topLevelFormat(app, fileID)
This in turn calls recursiveFormat(app, fileType, fIn, fOut)
which returns the file object (and in dev mode a formatted version of that file)
NOTE : The code does not read everything perfectly and may not read some files properly. The code can be taken as a basis for the formatting of the file but is far from perfect in many cases

'''


'''
TODO
move checkbyte, fileID and fileType so it is always called rather than each function calling it

'''

dev = 'dev' in sys.argv
if dev:
	# TODO
	formatLog = {}

def fOutWrite(fOut, val, indentCount = 0):
	if fOut is not None:
		fOut.write('{}{}'.format(indentCount*indentCharacter, val))

def hexSpaces(string):
	return ' '.join([binascii.hexlify(s).upper() for s in string])
	
def readStr(fIn, fOut, b, indentCount = 0):
	val = fIn.read(b)
	if len(val) != b:
		raise Exception('Reached End Of File')
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(val))
		fOut.write('\n')
	return LE2BE2(val)
	
def readID(app, fIn, fOut, indentCount = 0):
	val = fIn.read(8)
	if len(val) != 8:
		raise Exception('Reached End Of File')
	fileID = struct.unpack('<Q', val)[0]
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(val))
		fOut.write('\t\t')
		data = app.tempNewFiles(fileID)
		if data is None:
			fOut.write('Unknown File ID')
		else:
			fOut.write(data["fileName"])
			fOut.write('\t\t')
			fOut.write(data["fileType"])
		fOut.write('\n')
	return fileID

def readType(fIn, fOut, indentCount = 0, fileType=None):
	if fileType is None:
		fileType = fIn.read(4)
	if len(fileType) != 4:
		raise Exception('Reached End Of File')
	if fOut is not None:
		ft = hexSpaces(fileType)
		fOut.write(indentCount*indentCharacter + ft)
		ft = ft.replace(' ','')
		
		if ft in fileTypes:
			fOut.write('\t\t{}'.format(fileTypes[ft]))
		else:
			fOut.write('\t\tUndefined')
		fOut.write('\n')
	return LE2BE2(fileType)

def readInt(fIn, fOut, b, indentCount = 0):
	# phase this out in favour of other functions
	count = fIn.read(b)
	if len(count) != b:
		raise Exception('Reached End Of File')
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(count))
		fOut.write('\t\t')
		fOut.write(str(LE2DEC2(count)))
		fOut.write('\n')
	return LE2DEC2(count)

def readInt16(fIn, fOut, indentCount = 0):
	count = fIn.read(2)
	if len(count) != 2:
		raise Exception('Reached End Of File')
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(count))
		fOut.write('\t\t')
		fOut.write(str(int16(count)))
		fOut.write('\n')
	return int16(count)

def readUInt16(fIn, fOut, indentCount = 0):
	count = fIn.read(2)
	if len(count) != 2:
		raise Exception('Reached End Of File')
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(count))
		fOut.write('\t\t')
		fOut.write(str(uint16(count)))
		fOut.write('\n')
	return uint16(count)

def readInt32(fIn, fOut, indentCount = 0):
	count = fIn.read(4)
	if len(count) != 4:
		raise Exception('Reached End Of File')
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(count))
		fOut.write('\t\t')
		fOut.write(str(int32(count)))
		fOut.write('\n')
	return int32(count)

def readUInt32(fIn, fOut, indentCount = 0):
	count = fIn.read(4)
	if len(count) != 4:
		raise Exception('Reached End Of File')
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(count))
		fOut.write('\t\t')
		fOut.write(str(uint32(count)))
		fOut.write('\n')
	return uint32(count)
	
def readFloat32(fIn, fOut, indentCount = 0):
	val = fIn.read(4)
	if len(val) != 4:
		raise Exception('Reached End Of File')
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(val))
		fOut.write('\t\t')
		fOut.write(str(float32(val)))
		fOut.write('\n')
	return float32(val)
	
def ReadRest(fIn, fOut, indentCount = 0):
	val = fIn.read()
	if fOut is not None:
		fOut.write(indentCount*indentCharacter + hexSpaces(val))
	return BEHEX2(val)

def cleverFormat(fIn, fOut, indentCount = 0):
	val = fIn.read()
	if fOut is not None:
		pointer1 = 0
		pointer2 = 0
		while pointer2 <= len(val)-4:
			mightBeAFileType = val[pointer2:pointer2+4]
			if BEHEX2(mightBeAFileType) in fileTypes:
				fOut.write(indentCount*indentCharacter + hexSpaces(val[pointer1:pointer2]))
				fOut.write('\n')
				readType(fIn, fOut, fileType=mightBeAFileType, indentCount=indentCount)
				pointer1 = pointer2 + 4
				pointer2 += 4
			else:
				pointer2 += 1
		fOut.write(indentCount*indentCharacter + hexSpaces(val[pointer1:]))
	return BEHEX2(val)

unsupportedTypes = ['3F742D26']

def topLevelFormat(app, fileID):
	'''
	:param app:
	:param fileID: integer value of the fileID
	:return:
	'''
	global success
	success = True
	indentCount = 0

	data = app.tempNewFiles(fileID)
	if data is None:
		raise Exception('Error with file "{}"'.format(fileID))
	app.log.info(__name__, 'Formatting {}:{}'.format(fileID, data["fileName"]))
	fIn = app.misc.FileObject()
	fIn.write(app.tempNewFiles.get_file(fileID))
	fIn.seek(0)

	if dev:
		fOut = app.misc.FileObject()
	else:
		fOut = None
	
	fileContainer = {}
	
	# file header
	readStr(fIn, fOut, 2)
	
	try:
		subFileContainer = recursiveFormat(app, fIn, fOut, indentCount)
		for key in subFileContainer:
			fileContainer[key] = subFileContainer[key]
	except Exception as e:
		print('{}, {}'.format(e.message, e.args))
		fileContainer['fileID'] = fileID
		fileContainer['fileType'] = data["fileType"]
		success = False
	
	# fileContainer['readRest'] = ReadRest(fIn, fOut)
	fileContainer['readRest'] = cleverFormat(fIn, fOut)
	if dev:
		if fileContainer['fileType'] not in formatLog:
			formatLog[fileContainer['fileType']] = {}
			formatLog[fileContainer['fileType']]['success'] = 0
			formatLog[fileContainer['fileType']]['fail'] = 0
		if fileContainer['readRest'] == '' and success:
			formatLog[fileContainer['fileType']]['success'] += 1
		else:
			formatLog[fileContainer['fileType']]['fail'] += 1
			success = False

		with open('./formatLog.json', 'w') as f:
			json.dump(formatLog, f)

	if dev:
		print(data['fileName'])
		if not success and fileContainer['fileType'] not in unsupportedTypes:
			if not os.path.isdir(os.path.join(app.CONFIG['dumpFolder'], app.gameFunctions.gameIdentifier, data['forgeFile'])):
				os.makedirs(os.path.join(app.CONFIG['dumpFolder'], app.gameFunctions.gameIdentifier, data['forgeFile']))
			outPath = os.path.join(app.CONFIG['dumpFolder'], app.gameFunctions.gameIdentifier, data['forgeFile'], '{}{}.format'.format(data['fileName'], time.time()))
			fOut.save(outPath, 'w')
			os.startfile('explorer "{}"'.format(outPath))
	return fileContainer
	
def recursiveFormat(app, fIn, fOut, indentCount=0):
	global success
	
	fileContainer = {}

	fileContainer['fileID'] = readID(app, fIn, fOut, indentCount)
	fileType = readType(fIn, fOut, indentCount=indentCount+1)
	indentCount += 1
	fileContainer['fileType'] = fileType
	# fOutWrite(fOut, '\n')

	app.log.info(__name__, 'Formatting Type: {}'.format(fileType))
	if dev:
		if not os.path.isdir(os.path.join(app.CONFIG['dumpFolder'], 'fileTypes')):
			os.makedirs(os.path.join(app.CONFIG['dumpFolder'], 'fileTypes'))
		typeOut = open(os.path.join(app.CONFIG['dumpFolder'], 'fileTypes', fileType), 'a')
		filePointer = fIn.tell()
		fIn.seek(-12, 1)
		typeOut.write(hexSpaces(fIn.read()))
		typeOut.write('\n')
		typeOut.close()
		fIn.seek(filePointer)
	
	if fileType == "0984415E": #entity
		# # data
		# checkByte1 = readInt(fIn, fOut, 1) # checkbyte 03 to continue (other stuff to not? have seen 00 with data after)
		# if checkByte1 != 3:
			# print 'check byte not 3'
			# return fileContainer
		# fileContainer['transformationMtx'] = [[],[],[],[]]
		# # 4x4 transformation matrix
		# fOutWrite(fOut, '\nTransformation Matrix\n')
		# for _ in range(4):
			# for m in range(4):
				# fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut))
		# fOutWrite(fOut, '\n')
		
		# # jump to mesh
		# filePointer = fIn.tell()
		# rawFile = fIn.read()
		# bbloc = rawFile.find('\x3B\x96\x6E\x53')
		# if bbloc == -1:
			# return fileContainer
		# fIn.seek(filePointer)
		# readStr(fIn, fOut, bbloc-8)
		
		# readID(app, fIn, fOut)
		# fileType2 = readType(fIn, fOut)
		# subFileContainer = recursiveFormat(app, fileType2, fIn, fOut)
		# if fileType2 == '536E963B':
			# fileContainer['fileIDList'] = {}
			# # fileContainer['fileIDList'].append(subFileContainer['LOD'])
			# # fileContainer['LOD'].append({'fileID':readID(app, fIn, fOut)})
			# if subFileContainer['meshID'] not in fileContainer['fileIDList']:
				# fileContainer['fileIDList'][subFileContainer['meshID']] = []
			# if len(subFileContainer['tm']) != len(subFileContainer['BB']):
				# raise Exception('should these be the same size?')
			# for a in range(len(subFileContainer['tm'])):
				# fileContainer['fileIDList'][subFileContainer['meshID']].append(
					# {
					# 'tm':[fileContainer['transformationMtx']]+[subFileContainer['tm'][a]]
					# }
				# )
			# if len(subFileContainer['tm']) == 0:
				# fileContainer['fileIDList'][subFileContainer['meshID']].append(
					# {
					# 'tm':[fileContainer['transformationMtx']]
					# }
				# )
			# # fileContainer['meshID']
			# # fileContainer['tm'].append([])
			# # fileContainer['BB'].append([])
		
		# filePointer = fIn.tell()
		# rawFile = fIn.read()
		# bbloc = rawFile.find('\x76\x34\xEC\x4A')
		# if bbloc == -1:
			# raise Exception()
		# fIn.seek(filePointer)
		# readStr(fIn, fOut, bbloc-8)
		
		# fOutWrite(fOut, '\n')
		
		# # data layer filter
		# # 4 count, more data in here sometimes
		# for _ in range(3):
			# readID(app, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# subFileContainer2 = recursiveFormat(app, fileType2, fIn, fOut)
			# if fileType2 == '4AEC3476':
				# BB = subFileContainer2['BB']
				# for a in fileContainer['fileIDList']:
					# for b in fileContainer['fileIDList'][a]:
						# b['BB'] = BB
				
		
		# # 03 end file?
		# readStr(fIn, fOut, 1)
		# fOutWrite(fOut, '\n')
		# return fileContainer
		
		
		
		
		
		
		
		# original full code below
		
		
		# data
		checkByte = readStr(fIn, fOut, 1, indentCount) # checkbyte 03 to continue (other stuff to not? have seen 00 with data after)
		if checkByte == '00':
			for _ in range(2):
				recursiveFormat(app, fIn, fOut, indentCount+1)
		fileContainer['transformationMtx'] = [[],[],[],[]]
		# 4x4 transformation matrix
		fOutWrite(fOut, '\n', indentCount)
		fOutWrite(fOut, 'Transformation Matrix\n', indentCount)
		for _ in range(4):
			for m in range(4):
				fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut, indentCount))
		fOutWrite(fOut, '\n')
		count1 = readUInt32(fIn, fOut, indentCount)
		if count1 > 10000:
			app.log.warn(__name__, 'error reading entity file')
			# convert to an actual logger
			success = False
			return fileContainer
		
		fileContainer['unknown'] = []
		
		subFileContainer = {}

		try:
			for _ in range(count1):
				fOutWrite(fOut, '\n')
				if readStr(fIn, fOut, 2, indentCount+1) not in ['0004','0100']: # 04 00
					if dev:
						try:
							success = False
							formatLog[fileType2]['fail'] += 1
						except:
							pass
					fOutWrite(fOut, 'formatting issue\n')
					break
				elif dev:
					try:
						formatLog[fileType2]['success'] += 1
					except:
						pass
				subFileContainer = recursiveFormat(app, fIn, fOut, indentCount+1)
				fileType2 = subFileContainer['fileType']
				if dev and fileType2 not in formatLog:
					formatLog[fileType2] = {}
					formatLog[fileType2]['success'] = 0
					formatLog[fileType2]['fail'] = 0


				# for key in subFileContainer:
					# if key in fileContainer:
						# fileContainer[key] += subFileContainer[key]
					# else:
						# fileContainer[key] = subFileContainer[key]
		except:
			pass





			
		# float * 7
		
		# 37 bytes
		# 2 bytes
		# float
		
		# bouding box
		# id
		# type
		# float32 * 6
		# int32
		
		# entity descriptor
		# 19 bytes
		
		filePointer = fIn.tell()
		rawFile = fIn.read()
		bbloc = rawFile.find('\x76\x34\xEC\x4A')
		if bbloc == -1:
			raise Exception()
		fIn.seek(filePointer)
		if bbloc-8-43 == 0:
			fOutWrite(fOut, 'perfect formatting')
			if dev:
				try:
					formatLog[fileType2]['success'] += 1
				except:
					pass
		else:
			if dev:
				try:
					formatLog[fileType2]['fail'] += 1
					success = False
				except:
					pass
			fOutWrite(fOut, 'error formatting\n')
		readStr(fIn, fOut, bbloc-8-43)
		
		fOutWrite(fOut, '\n')
		
		readStr(fIn, fOut, 43)
		
		# data layer filter
		# 4 count, more data in here sometimes
		for _ in range(3):
			recursiveFormat(app, fIn, fOut)
		
		# 03 end file?
		checkByte2 = readStr(fIn, fOut, 1)
		if checkByte2 == '00':
			recursiveFormat(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == "3F742D26":	# entity group
		# cheap method
		# read top transformation matrix
		# jump to next 29 8D 65 EC while in file
			# jump to next 3B 96 6E 53
			# read 3B 96 6E 53
		checkByte1 = readInt(fIn, fOut, 1)
		if checkByte1 == 0:
			app.log.warn(__name__, 'checkbyte is not 3')
			return fileContainer
		fileContainer['transformationMtx'] = [[],[],[],[]]
		for _ in range(4):
			for m in range(4):
				fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut))
		fOutWrite(fOut, '\n')
		
		fileContainer['fileIDList'] = {}
		
		filePointer = fIn.tell()
		rawFile = fIn.read()
		visualLoc = rawFile.find('\x29\x8D\x65\xEC')

		while visualLoc != -1:
			fIn.seek(filePointer)
			readStr(fIn, fOut, visualLoc-8)
			
			# jump to mesh
			filePointer = fIn.tell()
			rawFile = fIn.read()
			bbloc = rawFile.find('\x3B\x96\x6E\x53')
			if bbloc == -1:
				return fileContainer
			fIn.seek(filePointer)
			readStr(fIn, fOut, bbloc-8)

			subFileContainer = recursiveFormat(app, fIn, fOut)
			if subFileContainer['meshID'] not in fileContainer['fileIDList']:
				fileContainer['fileIDList'][subFileContainer['meshID']] = []
			if len(subFileContainer['tm']) != len(subFileContainer['BB']):
				raise Exception('should these be the same size?')
			for a in range(len(subFileContainer['tm'])):
				fileContainer['fileIDList'][subFileContainer['meshID']].append(
					{
					'tm':[fileContainer['transformationMtx']]+[subFileContainer['tm'][a]],
					'BB':subFileContainer['BB']
					}
				)
			if len(subFileContainer['tm']) == 0:
				fileContainer['fileIDList'][subFileContainer['meshID']].append(
					{
					'tm':[fileContainer['transformationMtx']]
					}
				)
			
			
			
					
			filePointer = fIn.tell()
			rawFile = fIn.read()
			visualLoc = rawFile.find('\x29\x8D\x65\xEC')		
			
		fIn.seek(filePointer)

			
			
			
			
			
		# checkByte1 = readInt(fIn, fOut, 1)
		# if checkByte1 == 0:
			# readID(app, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(app, fileType2, fIn, fOut)
			# readID(app, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(app, fileType2, fIn, fOut)
		# fileContainer['transformationMtx'] = [[],[],[],[]]
		# for _ in range(4):
			# for m in range(4):
				# fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut))
		# fOutWrite(fOut, '\n')
		# count1 = readUInt32(fIn, fOut)
		# for _ in range(count1):
			# readStr(fIn, fOut, 2)
			# readID(app, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(app, fileType2, fIn, fOut)
		
		
		# readStr(fIn, fOut, 43)
		
		# for _ in range(3):
			# readID(app, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(app, fileType2, fIn, fOut)
		# fOutWrite(fOut, '\n')
		# return fileContainer
	
	elif fileType == "E6545731": # mission root
		count1 = readUInt32(fIn, fOut)
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			readID(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		count2 = readUInt32(fIn, fOut)
		for _ in range(count2):
			readStr(fIn, fOut, 2)
			recursiveFormat(app, fIn, fOut)
	
	elif fileType == "414FF9F7": # mission context
		readStr(fIn, fOut, 1)
		count1 = readUInt32(fIn, fOut)
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			readID(app, fIn, fOut)
			readType(fIn, fOut)
			readStr(fIn, fOut, 4)
			fOutWrite(fOut, '\n')
		fOutWrite(fOut, '\n')
	
	elif fileType == "1CBDE084":
		readStr(fIn, fOut, 2)
		readID(app, fIn, fOut)
		fOutWrite(fOut, '\n')

		for _ in range(2):
			recursiveFormat(app, fIn, fOut)
		
		fileContainer['transformationMtx'] = [[],[],[],[]]
		for _ in range(4):
			for m in range(4):
				fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut))
		fOutWrite(fOut, '\n')
		
		count1 = readUInt32(fIn, fOut)
		
		fileContainer['files'] = []
		
		for _ in range(count1):
			readStr(fIn, fOut, 1)
			# readID(app, fIn, fOut)
			fileContainer['files'].append(readID(app, fIn, fOut))
		fOutWrite(fOut, '\n')
		
	elif fileType == "55AF1C3E":
		readStr(fIn, fOut, 2)
		count1 = readUInt32(fIn, fOut)
		for _ in range(count1):
			readStr(fIn, fOut, 41)
		count2 = readUInt32(fIn, fOut)
		readStr(fIn, fOut, 12*count2)
		for _ in range(2):
			recursiveFormat(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	
	elif fileType == "2D675BA2":	# merged shape
		count1 = readUInt32(fIn, fOut) # possibly a count
		if count1 != 0:
			app.log.warn(__name__, '"2D675BA2" count1 is not 0')
			return fileContainer
		count2 = readUInt32(fIn, fOut)
		for _ in range(count2):
			readStr(fIn, fOut, 2)
			readID(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		count3 = readUInt32(fIn, fOut)
		fOutWrite(fOut, '\n')
		for _ in range(count3):	# transformation matrix
			for a in range(16):
				readFloat32(fIn, fOut)
			fOutWrite(fOut, '\n')
			
		count4 = readUInt32(fIn, fOut)
		fOutWrite(fOut, '\n')
		for _ in range(count4):
			recursiveFormat(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == "43EF99C2":	#Collision Filter Info 
		readStr(fIn, fOut, 15)
		fOutWrite(fOut, '\n')
	
	elif fileType == "AC2BBF68":	# datablock
		count1 = readUInt32(fIn, fOut)
		fileContainer['dataBlock'] = []
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			fileContainer['dataBlock'].append(readID(app, fIn, fOut))
		fOutWrite(fOut, '\n')
		count2 = readUInt32(fIn, fOut) # seems to be about the same or slightly less than count1
		readUInt32(fIn, fOut) # this might be a 64 bit int
		readStr(fIn, fOut, 4)
	
	elif fileType == "EC658D29":	# visual
		readStr(fIn, fOut, 4)
		readID(app, fIn, fOut)
		# fOutWrite(fOut, '\n')
		
		subFileContainer = {}
		
		ending0 = readStr(fIn, fOut, 1)
		
		# this totally isn't the correct way to read this but I 
		# can't work out how many sub-files should be read and
		# this is the only way I can work out how to do it.
		# while ending0 == '00':
			# readID(app, fIn, fOut) # temporary id?
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(app, fileType2, fIn, fOut)
			# ending0 = readStr(fIn, fOut, 1)
		# while ending0 == '03':
			# ending0 = readStr(fIn, fOut, 1)
		recursiveFormat(app, fIn, fOut)
		ending0 = readStr(fIn, fOut, 1)
		
		fOutWrite(fOut, '\n')
		
		for _ in range(7):
			readFloat32(fIn, fOut)
	
	elif fileType == "01437462":	# LOD selector
		readStr(fIn, fOut, 1)
		readID(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		for _ in range(5):
			ending0 = readStr(fIn, fOut, 1)
			if ending0 == '00':
				recursiveFormat(app, fIn, fOut)
			elif ending0 != '03':
				raise Exception()
		# while ending0 == '00':
		#
		# 	ending0 = readStr(fIn, fOut, 1)
		# while ending0 == '03':
		# 	ending0 = readStr(fIn, fOut, 1)
	
	elif fileType == "536E963B":	# mesh instance data
		readStr(fIn, fOut, 1)
		fileContainer['meshID'] = readID(app, fIn, fOut)
		readStr(fIn, fOut, 40) #contains a compiled mesh instance 4368101B
		count1 = readUInt32(fIn, fOut) # number of textures to follow
		fOutWrite(fOut, '\n')
		for n in range(count1):
			readStr(fIn, fOut, 1)
			recursiveFormat(app, fIn, fOut)
		
		# readStr(fIn, fOut, 8) # two counts. first count for transformation matrix. second for more things?
		count2 = readUInt32(fIn, fOut)
		if count2 > 10000:
			app.log.warn(__name__, 'count2:{} is too large. Aborting'.format(count2))
			return fileContainer
		fileContainer['tm'] = []
		for _ in range(count2):
			transformationMtx = [[],[],[],[]]
			for _ in range(4):
				for m in range(4):
					transformationMtx[m].append(readFloat32(fIn, fOut))
			fileContainer['tm'].append(transformationMtx)
			fOutWrite(fOut, '\n')
		count3 = readUInt32(fIn, fOut)
		if count3 > 10000:
			raise Exception('count3 is too large. Aborting')
		fileContainer['BB'] = []
		for _ in range(count3):
			subFileContainer = recursiveFormat(app, fIn, fOut)
			fileType2 = subFileContainer['fileType']
			if fileType2 == '4AEC3476':
				fileContainer['BB'].append(subFileContainer['BB'])
		fOutWrite(fOut, '\n')
		
		# needs to return {'fileID':'', 'tm':[], 'BB':[]}
		
	elif fileType == "7270FC9D":
		count1 = readUInt32(fIn, fOut)
		for _ in range(count1):
			readStr(fIn, fOut, 1)
			readID(app, fIn, fOut)
			
	elif fileType == "995BFBF5":
		readStr(fIn, fOut, 1)
		readID(app, fIn, fOut)
		readStr(fIn, fOut, 1)
		readID(app, fIn, fOut)
		readStr(fIn, fOut, 2)
		readID(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == "132FE22D":
		# needs more work
		readStr(fIn, fOut, 3)
		readID(app, fIn, fOut)
		count1 = readUInt32(fIn, fOut)
		for _ in range(count1+1):
			readStr(fIn, fOut, 1) #may contain a count
			readID(app, fIn, fOut)
		readStr(fIn, fOut, 4*9)
		fOutWrite(fOut, '\n')
		
	elif fileType == "BE711F06":
		readStr(fIn, fOut, 1) #00
		fOutWrite(fOut, '\n')
		
	elif fileType == "2AA179AB":
		readStr(fIn, fOut, 1)
		fOutWrite(fOut, '\n')
		
	elif fileType == 'B8B08A89':
		readStr(fIn, fOut, 1)
		readID(app, fIn, fOut)
		fOutWrite(fOut, '\n')
	
	elif fileType == "2E8B5553":	# Event Listener 
		# readStr(fIn, fOut, 2)
		fOutWrite(fOut, '\n')
		
	elif fileType == '4AEC3476':	# bounding volume / bounding box
		fileContainer['BB'] = {}
		fileContainer['BB']['minx'] = readFloat32(fIn, fOut)
		fileContainer['BB']['miny'] = readFloat32(fIn, fOut)
		fileContainer['BB']['minz'] = readFloat32(fIn, fOut)
		fileContainer['BB']['maxx'] = readFloat32(fIn, fOut)
		fileContainer['BB']['maxy'] = readFloat32(fIn, fOut)
		fileContainer['BB']['maxz'] = readFloat32(fIn, fOut)
		readUInt32(fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == '60121A9E':	# Entity Descriptor
		readStr(fIn, fOut, 19)
		fOutWrite(fOut, '\n')
		
	elif fileType == 'DB1D406E':	# Data Layer Filter 
		count1 = readUInt32(fIn, fOut) #count
		# more data follows this if count != 0
		for _ in range(count1):
			recursiveFormat(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == 'E31593E1':
		readStr(fIn, fOut, 1)
		readID(app, fIn, fOut)
		readStr(fIn, fOut, 4)
		fOutWrite(fOut, '\n')
	
	elif fileType == '55AF1C3E':	# unknown
		readStr(fIn, fOut, 2)
		count1 = readUInt32(fIn, fOut)
		
		if count1 > 100:
			app.log.warn(__name__, 'error reading unknown file type')
			# convert to an actual logger
			return fileContainer
		for _ in range(count1):
			recursiveFormat(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		
		count2 = readUInt32(fIn, fOut)
		if count2 > 100:
			app.log.warn(__name__, 'error reading unknown file type')
			# convert to an actual logger
			return fileContainer
		for _ in range(count2):
			readStr(fIn, fOut, 12)
		fOutWrite(fOut, '\n')
		
	elif fileType == '554C614C':	# unknown
		readStr(fIn, fOut, 1)
		readID(app, fIn, fOut)
		readStr(fIn, fOut, 2)
		fOutWrite(fOut, '\n')

		recursiveFormat(app, fIn, fOut)
		
		fOutWrite(fOut, '\n')
		
	elif fileType == 'AA8F96B6':	# unknown
		readStr(fIn, fOut, 11)
		for _ in range(5):
			readFloat32(fIn, fOut)
		readStr(fIn, fOut, 10)
		# readStr(fIn, fOut, 1)
		fOutWrite(fOut, '\n')
		
	elif fileType == '344FA659':	# unknown
		readStr(fIn, fOut, 29)
		fOutWrite(fOut, '\n')
		
	elif fileType == '788BAA0D':	# unknown
		for _ in range(4):
			for _ in range(4):
				readFloat32(fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == '709FB9D4':	# unknown
		readStr(fIn, fOut, 13)
		fOutWrite(fOut, '\n')
		
	elif fileType == '3BBECB2B':	# unknown
		readStr(fIn, fOut, 11)
		count1 = readUInt32(fIn, fOut)
		for _ in range(count1):
			recursiveFormat(app, fIn, fOut)
			
		# 1.1 in float
			# 4 bytes
			# count
				# 00
				# fileID
		# 1.5 in float
			
		# 2.1 in float
			# count?
				# 00
				# fileID
			# 4 bytes
		# 3 in float
			# count
				# 00
				# fileID
			# count
				# 00
				# fileID
			
		readStr(fIn, fOut, 4) # float
		for _ in range(2):
			count2 = readUInt32(fIn, fOut)
			if count2 > 10000:
				app.log.warn(__name__, 'error reading entity file')
				# convert to an actual logger
				return fileContainer
			for _ in range(count2):
				readStr(fIn, fOut, 1)
				readID(app, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == 'C8C23780':	# unknown
		readStr(fIn, fOut, 16)
		# three floats and zeros
		fOutWrite(fOut, '\n')

	elif fileType == '509C4552':
		readStr(fIn, fOut, 8)
		readStr(fIn, fOut, 4*4) #4 floats
		readStr(fIn, fOut, 4)
		fOutWrite(fOut, '\n')
		
	elif fileType == '4661AAEF': #needs work
		readStr(fIn, fOut, 2)
		count1 = readUInt32(fIn, fOut)
		readStr(fIn, fOut, 2*count1)
		readStr(fIn, fOut, 4*6) #6 floats
		count2 = readUInt32(fIn, fOut)
		for _ in range(count2):
			readStr(fIn, fOut, 24)
		readStr(fIn, fOut, 1)
		fOutWrite(fOut, '\n')

	elif fileType == '2132CC6E':
		readStr(fIn, fOut, 12, indentCount)
		checkByte = readStr(fIn, fOut, 1, indentCount)
		recursiveFormat(app, fIn, fOut, indentCount)

	elif fileType == '21795599':
		for l in [2,2,1,1,4,2,2]:
			count = readUInt32(fIn, fOut, indentCount)
			readStr(fIn, fOut, count*l, indentCount+1)
		count2 = 0
		count3 = 0
		count4 = 0
		# probably not right but this seems to work
		while count2 < count or count3 != count4:
			checkByte = readStr(fIn, fOut, 1, indentCount)
			count4 += 1
			if checkByte == '00':
				subFileContainer = recursiveFormat(app, fIn, fOut, indentCount)
				count2 += subFileContainer['count']
				count3 += 2
			elif checkByte == '03':
				continue
			else:
				raise Exception()
		checkByte = readStr(fIn, fOut, 1, indentCount)
		if checkByte != '03':
			raise Exception()
		readStr(fIn, fOut, 8, indentCount)
		count = readUInt32(fIn, fOut)
		for _ in range(count):
			checkByte = readStr(fIn, fOut, 1)
			recursiveFormat(app, fIn, fOut)
		count = readUInt32(fIn, fOut)
		for _ in range(count):
			readStr(fIn, fOut, 4)
		readStr(fIn, fOut, 1)
		for _ in range(7):
			readStr(fIn, fOut, 4)
		recursiveFormat(app, fIn, fOut)

	elif fileType == '9336FC8B':
		readStr(fIn, fOut, 8*4, indentCount)
		count1 = readUInt32(fIn, fOut, indentCount)
		fileContainer['count'] = count1
		if count1 == 0:
			pass
		elif 0<count1<100000:
			readStr(fIn, fOut, count1 * 4, indentCount+1)
		else:
			raise Exception('Probably an issue here')
		count2 = readUInt32(fIn, fOut, indentCount)
		if count2 == 0:
			pass
		elif 0<count2<100000:
			readStr(fIn, fOut, count2, indentCount+1)
		else:
			raise Exception('Probably an issue here')

	elif fileType == '1FB7CB75':
		readStr(fIn, fOut, 61)

	elif fileType == 'F49B6117':
		readStr(fIn, fOut, 1)
		for _ in range(4):
			readStr(fIn, fOut, 4)
		count1 = readUInt32(fIn, fOut)
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			readID(app, fIn, fOut)

	elif fileType == '0E5A450A':
		# readStr(fIn, fOut, 184)
		readStr(fIn, fOut, 14)
		for _ in range(2):
			recursiveFormat(app, fIn, fOut)

	elif fileType == '228F402A':
		readStr(fIn, fOut, 29)
		readID(app, fIn, fOut)
		readStr(fIn, fOut, 17)
		fOutWrite(fOut, '\nTransformation Matrix\n')
		for _ in range(4):
			for _ in range(4):
				readFloat32(fIn, fOut)

	elif fileType == '1C4B22AA':
		readStr(fIn, fOut, 6)
		b = readInt(fIn, fOut, 1)
		if b == 3:
			readStr(fIn, fOut, 5)
			readID(app, fIn, fOut)
		elif b == 5:
			readID(app, fIn, fOut)
			readStr(fIn, fOut, 5)
			readID(app, fIn, fOut)
		else:
			app.log.warn(__name__, 'value is not 3 or 5 I don\'t know how to deal with this')

	elif fileType == 'A2B7E917':
		readStr(fIn, fOut, 52)
		recursiveFormat(app, fIn, fOut)

	elif fileType == '13237FE9':
		readStr(fIn, fOut, 48)
		readStr(fIn, fOut, readUInt32(fIn, fOut))

	elif fileType == '788BAA0D':
		for _ in range(16):
			readFloat32(fIn, fOut)

	elif fileType == '709FB9D4':
		readStr(fIn, fOut, 13)

	elif fileType == 'E8134060':    # Sound Component
		readStr(fIn, fOut, 2)
		for _ in range(3):
			recursiveFormat(app, fIn, fOut)
		readStr(fIn, fOut, 10) # wrong but needs more examples

	elif fileType == '0423BD15':    # Sound Emitter
		readStr(fIn, fOut, 24)

	elif fileType == '43F19E3B':    # Event Switch Dependencies
		readStr(fIn, fOut, 27)

	elif fileType == '4E7C39C3':    # Simple Sound Sub Component
		for _ in range(2):
			recursiveFormat(app, fIn, fOut)

	elif fileType == '89288371':
		pass

	elif fileType == '71FDA747':
		readStr(fIn, fOut, 4)
		readID(app, fIn, fOut)
		readStr(fIn, fOut, 33)

	elif fileType == 'B6373E87':
		readStr(fIn, fOut, 4)
		readID(app, fIn, fOut)
		readStr(fIn, fOut, 11)

	elif fileType == '9EF59664':
		readStr(fIn, fOut, 13)

	elif fileType == '5730D30E':
		recursiveFormat(app, fIn, fOut)

		count1 = readUInt32(fIn, fOut)
		for _ in range(count1):
			readStr(fIn, fOut, 12)

		count2 = readUInt32(fIn, fOut)
		if count2 != 0:
			success = False

	elif fileType == 'DAB4219F':
		pass

	elif fileType == '7313743E':
		count1 = readUInt32(fIn, fOut)
		readStr(fIn, fOut, 10)
		for _ in range(count1):
			recursiveFormat(app, fIn, fOut)

	elif fileType == '299309DE':
		readStr(fIn, fOut, 2)

	elif fileType == 'CFC81A8A':
		readStr(fIn, fOut, 2)

	elif fileType == 'B0438131':
		count1 = readUInt32(fIn, fOut)
		readStr(fIn, fOut, count1)

	elif fileType == 'EE568905':
		count1 = readUInt32(fIn, fOut, indentCount)
		for n in range(count1):
			readStr(fIn, fOut, 1, indentCount+1)
			fileID2 = readID(app, fIn, fOut, indentCount+1)
			app.gameFunctions.read_file(app, fileID2)
			print('{} of {}'.format(n, count1))

	# F9 C2 8F 68
	# F0 8C 38 D8
	# 63 6A 56 1D
	# 60 40 13 E8
	# 4C 61 4C 55
	# 06 1F 71 BE
	# 2B CB BE 3B
	# 6D 7F 3A 2F
	
	elif fileType == '':
		raise Exception()
	
	else:
		success = False
		fOutWrite(fOut, 'not currently supported\n')
		app.log.warn(__name__, '{} not currently supported'.format(fileType))
		raise Exception()
		return []
	return fileContainer