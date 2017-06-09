# if line starts with # read that number of bytes
	# if second character is : read to end of file
# if line starts with @
	# followed by 'id' read 8 bytes and look up id name
	# followed by 'type' read 4 bytes and look up file type
# if line starts with & print the text after (used for blank lines)
# if line starts with $ loop followed by number of bytes to read

def hexSpaces(string):
	import binascii
	return ' '.join([binascii.hexlify(s).upper() for s in string])
	
def readStr(fIn, fOut, b):
	fOut.write(hexSpaces(fIn.read(b)))
	fOut.write('\n')
	
def readID(fileTree, fileList, config, fIn, fOut):
	import binascii
	from misc import tempFiles
	fileID = hexSpaces(fIn.read(8))
	fOut.write(fileID)
	fOut.write('\t\t')
	fileID = fileID.replace(' ', '')
	if not tempFiles.exists(config, fileID):
		from ACUnity.decompressDatafile import decompressDatafile
		decompressDatafile(fileTree, fileList, config, fileID)
	data = tempFiles.read(config, fileID)
	if len(data) == 0:
		fOut.write('Unknown File ID')
	else:
		data = data[0]
		fOut.write(data["fileName"])
		fOut.write('\t\t')
		fOut.write(data["resourceType"])
	fOut.write('\n')

def readType(fIn, fOut):
	fileType = fIn.read(4)
	fOut.write(hexSpaces(fileType))
	fOut.write('\n')
	return hexSpaces(fileType[::-1]).replace(' ', '')

def readCount(fIn, fOut, b):
	count = fIn.read(b)
	fOut.write(hexSpaces(count))
	fOut.write('\n')
	return int(hexSpaces(count[::-1]).replace(' ', ''), 16)
	
def ReadRest(fIn, fOut):
	fOut.write(hexSpaces(fIn.read()))

def format(fileTree, fileList, config, fileID):
	from misc import tempFiles
	import os
	if not tempFiles.exists(config, fileID):
		from ACUnity.decompressDatafile import decompressDatafile
		decompressDatafile(fileTree, fileList, config, fileID)
	data = tempFiles.read(config, fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	print 'Formatting '+data["fileName"]
	fIn = open(data["dir"], 'rb')
	fOut = open(data["dir"]+'.format', 'w')
	
	# file header
	readStr(fIn, fOut, 2)
	readID(fileTree, fileList, config, fIn, fOut)
	readType(fIn, fOut)
	fOut.write('\n')
	
	recursiveFormat(fileTree, fileList, config, data["resourceType"], fIn, fOut)
	
	ReadRest(fIn, fOut)
		
	fIn.close()
	fOut.close()
	os.system(data["dir"]+'.format')
	
def recursiveFormat(fileTree, fileList, config, fileType, fIn, fOut):
	import os
	if not os.path.isdir(config['dumpFolder']+os.sep+'fileTypes'):
		os.makedirs(config['dumpFolder']+os.sep+'fileTypes')
	# typeOut = open(config['dumpFolder']+os.sep+'fileTypes'+os.sep+fileType, 'a')
	filePointer = fIn.tell()
	fIn.seek(-12, 1)
	# typeOut.write(hexSpaces(fIn.read()))
	# typeOut.write('\n')
	# typeOut.close()
	fIn.seek(filePointer)
	if fileType == "0984415E": #entity
		# data
		readStr(fIn, fOut, 1) # possibly a count
		readStr(fIn, fOut, 4)
		readStr(fIn, fOut, 16)
		readStr(fIn, fOut, 4)
		readStr(fIn, fOut, 16)
		readStr(fIn, fOut, 4)
		readStr(fIn, fOut, 16)
		readStr(fIn, fOut, 4)
		fOut.write('\n')
		count1 = readCount(fIn, fOut, 4) # possibly a count
		readStr(fIn, fOut, 2) # unknown
		fOut.write('\n')
		readID(fileTree, fileList, config, fIn, fOut) # temporary id?
		fileType2 = readType(fIn, fOut)
		recursiveFormat(fileTree, fileList, config, fileType2, fIn, fOut)
		
		for n in range(count1):
			readID(fileTree, fileList, config, fIn, fOut) # temporary id?
			fileType2 = readType(fIn, fOut)
			recursiveFormat(fileTree, fileList, config, fileType2, fIn, fOut)
		
		# readID(fileTree, fileList, config, fIn, fOut) # temporary id?
		# fileType2 = readType(fIn, fOut)
		# recursiveFormat(fileTree, fileList, config, fileType2, fIn, fOut)
		
		# readID(fileTree, fileList, config, fIn, fOut) # temporary id?
		# fileType2 = readType(fIn, fOut)
		# recursiveFormat(fileTree, fileList, config, fileType2, fIn, fOut)
		
		# readStr(fIn, fOut, 3)
		# readID(fileTree, fileList, config, fIn, fOut)
		# readStr(fIn, fOut, 6)
		# readID(fileTree, fileList, config, fIn, fOut)
		# readType(fIn, fOut)
		# readStr(fIn, fOut, 4)
		# readID(fileTree, fileList, config, fIn, fOut)
		# readStr(fIn, fOut, 1)
		# readID(fileTree, fileList, config, fIn, fOut)
		# readStr(fIn, fOut, 14)
		# readID(fileTree, fileList, config, fIn, fOut)
	
	elif fileType == "AC2BBF68":
		count1 = readCount(fIn, fOut, 4)
		for n in range(count1):
			readStr(fIn, fOut, 2)
			readID(fileTree, fileList, config, fIn, fOut)
	
	elif fileType == "EC658D29":	# visual
		readStr(fIn, fOut, 4)
		readID(fileTree, fileList, config, fIn, fOut)
		readStr(fIn, fOut, 1)
		fOut.write('\n')
	elif fileType == "01437462":	# LOD selector
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, config, fIn, fOut)
		readStr(fIn, fOut, 1)
		fOut.write('\n')
	elif fileType == "536E963B":	# mesh instance data
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, config, fIn, fOut)
		readStr(fIn, fOut, 40) #contains a compiled mesh instance 4368101B
		count1 = readCount(fIn, fOut, 4) # number of textures to follow
		readStr(fIn, fOut, 9)
		fOut.write('\n')
		for n in range(count1):
			readType(fIn, fOut)
			readStr(fIn, fOut, 1)		
			readID(fileTree, fileList, config, fIn, fOut)
			readStr(fIn, fOut, 1)
			readID(fileTree, fileList, config, fIn, fOut)
			readStr(fIn, fOut, 2)
			readID(fileTree, fileList, config, fIn, fOut)
			readStr(fIn, fOut, 9)
		
		
		fOut.write('\n')
	elif fileType == "132FE22D":
		readStr(fIn, fOut, 3)
		readID(fileTree, fileList, config, fIn, fOut)
		readStr(fIn, fOut, 5)
		readID(fileTree, fileList, config, fIn, fOut)
		readStr(fIn, fOut, 1)
		readID(fileTree, fileList, config, fIn, fOut)
		readStr(fIn, fOut, 5)
		#unfinished
		
	elif fileType == "BE711F06":
		readStr(fIn, fOut, 3)
		fOut.write('\n')
		
	elif fileType == "2AA179AB":
		readStr(fIn, fOut, 3)
		fOut.write('\n')
	
	elif fileType == "2E8B5553":
		readStr(fIn, fOut, 2)
		fOut.write('\n')
		
		
	else:
		fOut.write('not currently supported\n')
		print fileType+' not currently supported'