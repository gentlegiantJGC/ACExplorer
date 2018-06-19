import binascii, os, sys, json
from ACExplorer import CONFIG
from ACExplorer.misc import log
from ACExplorer.ACUnity.decompressDatafile import decompressDatafile
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import LE2BE2, BEHEX2, LE2DEC2, float32
fileTypes = json.load(open(r"./ACExplorer/ACUnity/fileFormats.json"))

'''
This module works by calling topLevelFormat(fileTree, fileList, fileID)
This in turn calls recursiveFormat(fileTree, fileList, fileType, fIn, fOut)
which returns the file object (and in dev mode a formatted version of that file)
NOTE : The code does not read everything perfectly and may not read some files properly. The code can be taken as a basis for the formatting of the file but is far from perfect in many cases

'''


'''
TODO
move checkbyte, fileID and fileType so it is always called rather than each function calling it

'''

dev = 'dev' in sys.argv
if dev:
	from ACExplorer import formatLog

def fOutWrite(fOut, val):
	if dev:
		fOut.write(val)

def hexSpaces(string):
	return ' '.join([binascii.hexlify(s).upper() for s in string])
	
def readStr(fIn, fOut, b):
	val = fIn.read(b)
	if len(val) != b:
		raise Exception('Reached End Of File')
	if dev:
		fOut.write(hexSpaces(val))
		fOut.write('\n')
	return LE2BE2(val)
	
def readID(fileTree, fileList, fIn, fOut):
	val = fIn.read(8)
	if len(val) != 8:
		raise Exception('Reached End Of File')
	fileID = BEHEX2(val)
	if dev:
		fOut.write(hexSpaces(val))
		fOut.write('\t\t')
		if not tempFiles.exists(fileID):
			decompressDatafile(fileTree, fileList, fileID)
		data = tempFiles.read(fileID)
		if len(data) == 0:
			fOut.write('Unknown File ID')
		else:
			data = data[0]
			fOut.write(data["fileName"])
			fOut.write('\t\t')
			fOut.write(data["resourceType"])
		fOut.write('\n')
	return fileID

def readType(fIn, fOut,fileType=None):
	if fileType is None:
		fileType = fIn.read(4)
	if len(fileType) != 4:
		raise Exception('Reached End Of File')
	if dev:
		ft = hexSpaces(fileType)
		fOut.write(ft)
		ft = ft.replace(' ','')
		
		if ft in fileTypes:
			fOut.write('\t\t'+fileTypes[ft])
		else:
			fOut.write('\t\tUndefined')
		fOut.write('\n')
	return LE2BE2(fileType)

def readInt(fIn, fOut, b):
	count = fIn.read(b)
	if len(count) != b:
		raise Exception('Reached End Of File')
	if dev:
		fOut.write(hexSpaces(count))
		fOut.write('\t\t')
		fOut.write(str(LE2DEC2(count)))
		fOut.write('\n')
	return LE2DEC2(count)
	
def readFloat32(fIn, fOut):
	val = fIn.read(4)
	if len(val) != 4:
		raise Exception('Reached End Of File')
	if dev:
		fOut.write(hexSpaces(val))
		fOut.write('\t\t')
		fOut.write(str(float32(val)))
		fOut.write('\n')
	return float32(val)
	
def ReadRest(fIn, fOut):
	val = fIn.read()
	if dev:
		fOut.write(hexSpaces(val))
	return BEHEX2(val)

def cleverFormat(fIn, fOut):
	val = fIn.read()
	if dev:
		pointer1 = 0
		pointer2 = 0
		while pointer2 <= len(val)-4:
			mightBeAFileType = val[pointer2:pointer2+4]
			if BEHEX2(mightBeAFileType) in fileTypes:
				fOut.write(hexSpaces(val[pointer1:pointer2]))
				fOut.write('\n')
				readType(fIn, fOut, mightBeAFileType)
				pointer1 = pointer2 + 4
				pointer2 += 4
			else:
				pointer2 += 1
		fOut.write(hexSpaces(val[pointer1:]))
	return BEHEX2(val)

def topLevelFormat(fileTree, fileList, fileID):
	global success
	success = True
	if not tempFiles.exists(fileID):
		decompressDatafile(fileTree, fileList, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	log.info(__name__, 'Formatting '+fileID+':'+data["fileName"])
	fIn = open(data["dir"], 'rb')
	if dev:
		fOut = open(data["dir"]+'.format', 'w')
	else:
		fOut = None
	
	fileContainer = {}
	
	# file header
	readStr(fIn, fOut, 2)
	fileContainer['fileID'] = readID(fileTree, fileList, fIn, fOut)
	fileContainer['fileType'] = readType(fIn, fOut)
	fOutWrite(fOut, '\n')
	
	try:
		subFileContainer = recursiveFormat(fileTree, fileList, data["resourceType"], fIn, fOut)
		for key in subFileContainer:
			fileContainer[key] = subFileContainer[key]
	except:
		pass
	
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
		
	fIn.close()
	if dev:
		fOut.close()
		print data["dir"]+'.format'
		if not success:
			os.system('explorer "{}.format"'.format(data['dir']))
	return fileContainer
	
def recursiveFormat(fileTree, fileList, fileType, fIn, fOut):
	global success
	log.info(__name__, 'Formatting Type: {}'.format(fileType))
	if dev:
		if not os.path.isdir(CONFIG['dumpFolder']+os.sep+'fileTypes'):
			os.makedirs(CONFIG['dumpFolder']+os.sep+'fileTypes')
		# typeOut = open(CONFIG['dumpFolder']+os.sep+'fileTypes'+os.sep+fileType, 'a')
		# filePointer = fIn.tell()
		# fIn.seek(-12, 1)
		# typeOut.write(hexSpaces(fIn.read()))
		# typeOut.write('\n')
		# typeOut.close()
		# fIn.seek(filePointer)
	
	fileContainer = {}
	
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
		
		# readID(fileTree, fileList, fIn, fOut)
		# fileType2 = readType(fIn, fOut)
		# subFileContainer = recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		# if fileType2 == '536E963B':
			# fileContainer['fileIDList'] = {}
			# # fileContainer['fileIDList'].append(subFileContainer['LOD'])
			# # fileContainer['LOD'].append({'fileID':readID(fileTree, fileList, fIn, fOut)})
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
			# readID(fileTree, fileList, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# subFileContainer2 = recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
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
		checkByte = readStr(fIn, fOut, 1) # checkbyte 03 to continue (other stuff to not? have seen 00 with data after)
		if checkByte == '00':
			for _ in range(2):
				readID(fileTree, fileList, fIn, fOut)
				fileType2 = readType(fIn, fOut)
				recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		fileContainer['transformationMtx'] = [[],[],[],[]]
		# 4x4 transformation matrix
		fOutWrite(fOut, '\nTransformation Matrix\n')
		for _ in range(4):
			for m in range(4):
				fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut))
		fOutWrite(fOut, '\n')
		count1 = readInt(fIn, fOut, 4) # possibly a count
		if count1 > 10000:
			log.warn(__name__, 'error reading entity file')
			# convert to an actual logger
			return fileContainer
		
		fileContainer['unknown'] = []
		
		subFileContainer = {}

		try:
			for _ in range(count1):
				fOutWrite(fOut, '\n')
				if readStr(fIn, fOut, 2) not in ['0004','0100']: # 04 00
					if dev:
						try:
							formatLog[fileType2]['fail'] += 1
							success = False
						except:
							pass
					fOutWrite(fOut, 'formatting issue\n')
					break
				elif dev:
					try:
						formatLog[fileType2]['success'] += 1
					except:
						pass
				readID(fileTree, fileList, fIn, fOut) # temporary id?
				fileType2 = readType(fIn, fOut)
				if dev and fileType2 not in formatLog:
					formatLog[fileType2] = {}
					formatLog[fileType2]['success'] = 0
					formatLog[fileType2]['fail'] = 0

				subFileContainer = recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
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
			readID(fileTree, fileList, fIn, fOut)
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		
		# 03 end file?
		readStr(fIn, fOut, 1)
		fOutWrite(fOut, '\n')
		
	elif fileType == "3F742D26":	# entity group
		# cheap method
		# read top transformation matrix
		# jump to next 29 8D 65 EC while in file
			# jump to next 3B 96 6E 53
			# read 3B 96 6E 53
		checkByte1 = readInt(fIn, fOut, 1)
		if checkByte1 == 0:
			log.warn(__name__, 'checkbyte is not 3')
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
			
			readID(fileTree, fileList, fIn, fOut)
			fileType2 = readType(fIn, fOut)
			subFileContainer = recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
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
			# readID(fileTree, fileList, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
			# readID(fileTree, fileList, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		# fileContainer['transformationMtx'] = [[],[],[],[]]
		# for _ in range(4):
			# for m in range(4):
				# fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut))
		# fOutWrite(fOut, '\n')
		# count1 = readInt(fIn, fOut, 4)
		# for _ in range(count1):
			# readStr(fIn, fOut, 2)
			# readID(fileTree, fileList, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		
		
		# readStr(fIn, fOut, 43)
		
		# for _ in range(3):
			# readID(fileTree, fileList, fIn, fOut)
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		# fOutWrite(fOut, '\n')
		# return fileContainer
	
	elif fileType == "E6545731": # mission root
		count1 = readInt(fIn, fOut, 4)
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			readID(fileTree, fileList, fIn, fOut)
		fOutWrite(fOut, '\n')
		count2 = readInt(fIn, fOut, 4)
		for _ in range(count2):
			readStr(fIn, fOut, 2)
			readID(fileTree, fileList, fIn, fOut)
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
	
	elif fileType == "414FF9F7": # mission context
		readStr(fIn, fOut, 1)
		count1 = readInt(fIn, fOut, 4)
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			readID(fileTree, fileList, fIn, fOut)
			readType(fIn, fOut)
			readStr(fIn, fOut, 4)
			fOutWrite(fOut, '\n')
		fOutWrite(fOut, '\n')
	
	elif fileType == "1CBDE084":
		readStr(fIn, fOut, 2)
		readID(fileTree, fileList, fIn, fOut)
		fOutWrite(fOut, '\n')
		
		readID(fileTree, fileList, fIn, fOut)
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		
		readID(fileTree, fileList, fIn, fOut)
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		
		fileContainer['transformationMtx'] = [[],[],[],[]]
		for _ in range(4):
			for m in range(4):
				fileContainer['transformationMtx'][m].append(readFloat32(fIn, fOut))
		fOutWrite(fOut, '\n')
		
		count1 = readInt(fIn, fOut, 4)
		
		fileContainer['files'] = []
		
		for _ in range(count1):
			readStr(fIn, fOut, 1)
			# readID(fileTree, fileList, fIn, fOut)
			fileContainer['files'].append(readID(fileTree, fileList, fIn, fOut))
		fOutWrite(fOut, '\n')
		
	elif fileType == "55AF1C3E":
		readStr(fIn, fOut, 2)
		count1 = readInt(fIn, fOut, 4)
		for _ in range(count1):
			readStr(fIn, fOut, 41)
		count2 = readInt(fIn, fOut, 4)
		readStr(fIn, fOut, 12*count2)
		for _ in range(2):
			readID(fileTree, fileList, fIn, fOut)
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	
	elif fileType == "2D675BA2":	# merged shape
		count1 = readInt(fIn, fOut, 4) # possibly a count
		if count1 != 0:
			log.warn(__name__, '"2D675BA2" count1 is not 0')
			return fileContainer
		count2 = readInt(fIn, fOut, 4)
		for _ in range(count2):
			readStr(fIn, fOut, 2)
			readID(fileTree, fileList, fIn, fOut)
		fOutWrite(fOut, '\n')
		count3 = readInt(fIn, fOut, 4)
		fOutWrite(fOut, '\n')
		for _ in range(count3):	# transformation matrix
			for a in range(16):
				readFloat32(fIn, fOut)
			fOutWrite(fOut, '\n')
			
		count4 = readInt(fIn, fOut, 4)
		fOutWrite(fOut, '\n')
		for _ in range(count4):
			readID(fileTree, fileList, fIn, fOut)
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == "43EF99C2":	#Collision Filter Info 
		readStr(fIn, fOut, 15)
		fOutWrite(fOut, '\n')
	
	elif fileType == "AC2BBF68":	# datablock
		count1 = readInt(fIn, fOut, 4)
		fileContainer['dataBlock'] = []
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			fileContainer['dataBlock'].append(readID(fileTree, fileList, fIn, fOut))
		fOutWrite(fOut, '\n')
		count2 = readInt(fIn, fOut, 4)
		if count2 != 1:
			log.warn(__name__, 'this value is normally 1')
			success = False
		readInt(fIn, fOut, 4) # this might be a 64 bit int
		readStr(fIn, fOut, 4)
	
	elif fileType == "EC658D29":	# visual
		readStr(fIn, fOut, 4)
		readID(fileTree, fileList, fIn, fOut)
		# fOutWrite(fOut, '\n')
		
		subFileContainer = {}
		
		ending0 = readStr(fIn, fOut, 1)
		
		# this totally isn't the correct way to read this but I 
		# can't work out how many sub-files should be read and
		# this is the only way I can work out how to do it.
		# while ending0 == '00':
			# readID(fileTree, fileList, fIn, fOut) # temporary id?
			# fileType2 = readType(fIn, fOut)
			# recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
			# ending0 = readStr(fIn, fOut, 1)
		# while ending0 == '03':
			# ending0 = readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut) # temporary id?
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		ending0 = readStr(fIn, fOut, 1)
		
		fOutWrite(fOut, '\n')
		
		for _ in range(7):
			readFloat32(fIn, fOut)
	
	elif fileType == "01437462":	# LOD selector
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut)
		fOutWrite(fOut, '\n')
		for _ in range(5):
			ending0 = readStr(fIn, fOut, 1)
			if ending0 == '00':
				readID(fileTree, fileList, fIn, fOut)  # temporary id?
				fileType2 = readType(fIn, fOut)
				recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
			elif ending0 != '03':
				raise Exception()
		# while ending0 == '00':
		#
		# 	ending0 = readStr(fIn, fOut, 1)
		# while ending0 == '03':
		# 	ending0 = readStr(fIn, fOut, 1)
	
	elif fileType == "536E963B":	# mesh instance data
		readStr(fIn, fOut, 1)
		fileContainer['meshID'] = readID(fileTree, fileList, fIn, fOut)
		readStr(fIn, fOut, 40) #contains a compiled mesh instance 4368101B
		count1 = readInt(fIn, fOut, 4) # number of textures to follow
		fOutWrite(fOut, '\n')
		for n in range(count1):
			readStr(fIn, fOut, 1)
			readID(fileTree, fileList, fIn, fOut) # temporary id?
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		
		# readStr(fIn, fOut, 8) # two counts. first count for transformation matrix. second for more things?
		count2 = readInt(fIn, fOut, 4)
		if count2 > 10000:
			log.warn(__name__, 'count2:{} is too large. Aborting'.format(count2))
			return fileContainer
		fileContainer['tm'] = []
		for _ in range(count2):
			transformationMtx = [[],[],[],[]]
			for _ in range(4):
				for m in range(4):
					transformationMtx[m].append(readFloat32(fIn, fOut))
			fileContainer['tm'].append(transformationMtx)
			fOutWrite(fOut, '\n')
		count3 = readInt(fIn, fOut, 4)
		if count3 > 10000:
			raise Exception('count3 is too large. Aborting')
		fileContainer['BB'] = []
		for _ in range(count3):
			readID(fileTree, fileList, fIn, fOut)
			fileType2 = readType(fIn, fOut)
			subFileContainer = recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
			if fileType2 == '4AEC3476':
				fileContainer['BB'].append(subFileContainer['BB'])
		fOutWrite(fOut, '\n')
		
		# needs to return {'fileID':'', 'tm':[], 'BB':[]}
		
	elif fileType == "7270FC9D":
		count1 = readInt(fIn, fOut, 4)
		for _ in range(count1):
			readStr(fIn, fOut, 1)
			readID(fileTree, fileList, fIn, fOut)
			
	elif fileType == "995BFBF5":
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut)
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut)
		readStr(fIn, fOut, 2)
		readID(fileTree, fileList, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == "132FE22D":
		# needs more work
		readStr(fIn, fOut, 3)
		readID(fileTree, fileList, fIn, fOut)
		count1 = readInt(fIn, fOut, 4)
		for _ in range(count1+1):
			readStr(fIn, fOut, 1) #may contain a count
			readID(fileTree, fileList, fIn, fOut)
		readStr(fIn, fOut, 4*9)
		fOutWrite(fOut, '\n')
		
	elif fileType == "BE711F06":
		readStr(fIn, fOut, 3)
		fOutWrite(fOut, '\n')
		
	elif fileType == "2AA179AB":
		readStr(fIn, fOut, 3)
		fOutWrite(fOut, '\n')
		
	elif fileType == 'B8B08A89':
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut)
		fOutWrite(fOut, '\n')
	
	elif fileType == "2E8B5553":	# Event Listener 
		readStr(fIn, fOut, 2)
		fOutWrite(fOut, '\n')
		
	elif fileType == '4AEC3476':	# bounding volume / bouding box
		fileContainer['BB'] = {}
		fileContainer['BB']['minx'] = readFloat32(fIn, fOut)
		fileContainer['BB']['miny'] = readFloat32(fIn, fOut)
		fileContainer['BB']['minz'] = readFloat32(fIn, fOut)
		fileContainer['BB']['maxx'] = readFloat32(fIn, fOut)
		fileContainer['BB']['maxy'] = readFloat32(fIn, fOut)
		fileContainer['BB']['maxz'] = readFloat32(fIn, fOut)
		readInt(fIn, fOut, 4)
		fOutWrite(fOut, '\n')
		
	elif fileType == '60121A9E':	# Entity Descriptor
		readStr(fIn, fOut, 19)
		fOutWrite(fOut, '\n')
		
	elif fileType == 'DB1D406E':	# Data Layer Filter 
		count1 = readInt(fIn, fOut, 4) #count
		# more data follows this if count != 0
		for _ in range(count1):
			readID(fileTree, fileList, fIn, fOut) # temporary id?
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		fOutWrite(fOut, '\n')
		
	elif fileType == 'E31593E1':
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut)
		readStr(fIn, fOut, 4)
		fOutWrite(fOut, '\n')
	
	elif fileType == '55AF1C3E':	# unknown
		readStr(fIn, fOut, 2)
		count1 = readInt(fIn, fOut, 4)
		
		if count1 > 100:
			log.warn(__name__, 'error reading unknown file type')
			# convert to an actual logger
			return fileContainer
		for _ in range(count1):
			readID(fileTree, fileList, fIn, fOut) # temporary id?
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		fOutWrite(fOut, '\n')
		
		count2 = readInt(fIn, fOut, 4)
		if count2 > 100:
			log.warn(__name__, 'error reading unknown file type')
			# convert to an actual logger
			return fileContainer
		for _ in range(count2):
			readStr(fIn, fOut, 12)
		fOutWrite(fOut, '\n')
		
	elif fileType == '554C614C':	# unknown
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut)
		readStr(fIn, fOut, 2)
		fOutWrite(fOut, '\n')
		
		readID(fileTree, fileList, fIn, fOut)
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		
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
		count1 = readInt(fIn, fOut, 4)
		for _ in range(count1):
			readID(fileTree, fileList, fIn, fOut) # temporary id?
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
			
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
			count2 = readInt(fIn, fOut, 4)
			if count2 > 10000:
				log.warn(__name__, 'error reading entity file')
				# convert to an actual logger
				return fileContainer
			for _ in range(count2):
				readStr(fIn, fOut, 1)
				readID(fileTree, fileList, fIn, fOut)
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
		count1 = readInt(fIn, fOut, 4)
		readStr(fIn, fOut, 2*count1)
		readStr(fIn, fOut, 4*6) #6 floats
		readStr(fIn, fOut, 29)
		fOutWrite(fOut, '\n')

	elif fileType == '2132CC6E':
		readStr(fIn, fOut, 12)
		checkByte = readStr(fIn, fOut, 1)
		readID(fileTree, fileList, fIn, fOut)  # temporary id?
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)

	elif fileType == '21795599':
		for l in [2,2,1,1,4,2,2]:
			count = readInt(fIn, fOut, 4)
			readStr(fIn, fOut, count*l)
		count2 = 0
		while count2 < count:
			checkByte = readStr(fIn, fOut, 1)
			if checkByte == '00':
				readID(fileTree, fileList, fIn, fOut)  # temporary id?
				fileType2 = readType(fIn, fOut)
				subFileContainer = recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
				count2 += subFileContainer['count']
			elif checkByte == '03':
				continue
			else:
				raise Exception()
		readStr(fIn, fOut, 8)
		count = readInt(fIn, fOut, 4)
		for _ in range(count):
			checkByte = readStr(fIn, fOut, 1)
			readID(fileTree, fileList, fIn, fOut)  # temporary id?
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)
		count = readInt(fIn, fOut, 4)
		for _ in range(count):
			readStr(fIn, fOut, 4)
		readStr(fIn, fOut, 1)
		for _ in range(7):
			readStr(fIn, fOut, 4)
		readID(fileTree, fileList, fIn, fOut)  # temporary id?
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)

	elif fileType == '9336FC8B':
		readStr(fIn, fOut, 8*4)
		count1 = readInt(fIn, fOut, 4)
		fileContainer['count'] = count1
		if 0<=count1<100000:
			readStr(fIn, fOut, count1 * 4)
		else:
			raise Exception('Probably an issue here')
		count2 = readInt(fIn, fOut, 4)
		if 0<count2<100000:
			readStr(fIn, fOut, count2)
			for _ in range(2):
				if readStr(fIn, fOut, 1) != '03':
					raise Exception('Expected "03"')
		elif count2 == 0:
			pass
		else:
			raise Exception('Probably an issue here')

	elif fileType == '1FB7CB75':
		readStr(fIn, fOut, 61)

	elif fileType == 'F49B6117':
		readStr(fIn, fOut, 1)
		for _ in range(4):
			readStr(fIn, fOut, 4)
		count1 = readInt(fIn, fOut, 4)
		for _ in range(count1):
			readStr(fIn, fOut, 2)
			readID(fileTree, fileList, fIn, fOut)

	elif fileType == '0E5A450A':
		# readStr(fIn, fOut, 184)
		readStr(fIn, fOut, 14)
		for _ in range(2):
			readID(fileTree, fileList, fIn, fOut)  # temporary id?
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)

	elif fileType == '228F402A':
		readStr(fIn, fOut, 29)
		readID(fileTree, fileList, fIn, fOut)
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
			readID(fileTree, fileList, fIn, fOut)
		elif b == 5:
			readID(fileTree, fileList, fIn, fOut)
			readStr(fIn, fOut, 5)
			readID(fileTree, fileList, fIn, fOut)
		else:
			log.warn(__name__, 'value is not 3 or 5 I don\'t know how to deal with this')

	elif fileType == 'A2B7E917':
		readStr(fIn, fOut, 52)
		readID(fileTree, fileList, fIn, fOut)  # temporary id?
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, fileType2, fIn, fOut)

	elif fileType == '13237FE9':
		readStr(fIn, fOut, 48)
		readStr(fIn, fOut, readInt(fIn, fOut, 4))

	elif fileType == '788BAA0D':
		for _ in range(16):
			readFloat32(fIn, fOut)

	elif fileType == '709FB9D4':
		readStr(fIn, fOut, 13)

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
		log.warn(__name__, fileType+' not currently supported')
		raise Exception()
		return []
	return fileContainer