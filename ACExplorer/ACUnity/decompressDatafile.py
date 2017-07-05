import os
import traceback

from ACExplorer import CONFIG
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import BE, BEHEX2, LE2BE, LE2BE2, LE2DEC, LE2DEC2
from ACExplorer.misc.decompress import decompress


def decompressDatafile(fileTree, fileList, fileID, forgeFile=None):
	fileID = fileID.upper()
	if forgeFile == None:
		for forgeFile in fileList:
			if fileID in fileList[forgeFile]:
				break
		if fileID not in fileList[forgeFile]:
			# with open(CONFIG["lightDict2"], 'r') as f:
				# lightDict = eval(f.read())
			# if fileID in lightDict:
				# for forgeFile in fileList:
					# if lightDict[fileID] in fileList[forgeFile]:
						# fileID = lightDict[fileID]
						# break
			# else:
				# return
				
			if fileID in os.listdir(CONFIG["lightDict"]):
				with open(CONFIG["lightDict"]+os.sep+fileID, 'r') as f:
					fileID2 = f.read()
				for forgeFile in fileList:
					if fileID2 in fileList[forgeFile]:
						fileID = fileID2
						break
			else:
				return
	if fileID not in fileList[forgeFile]:
		print fileID +' not found'
		traceback.print_stack()
		return
	if not os.path.isdir(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'raw'):
		os.makedirs(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'raw')
	uncompressedData = open(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'raw' + os.sep + 'temp', 'wb')
	f = open(CONFIG['ACUnityFolder']+os.sep+forgeFile, 'rb')
	f.seek(fileList[forgeFile][fileID]['rawDataOffset'])
	rawDataChunk = f.read(fileList[forgeFile][fileID]['rawDataSize'])
	f.close()
	if LE2BE(rawDataChunk, 0, 8) == '1004fa9957fbaa33': # if compressed
		compressionType = LE2DEC(rawDataChunk, 10, 1)
		compBlockCount = LE2DEC(rawDataChunk, 15, 4)
		compressedDataStart = 19+compBlockCount*4
		for m in xrange(compBlockCount):
			uncompressedSize = LE2DEC(rawDataChunk, 19+m*4, 2)
			compressedSize = LE2DEC(rawDataChunk, 21+m*4, 2)
			compressedData = BE(rawDataChunk, compressedDataStart+4, compressedSize)
			if uncompressedSize == compressedSize:
				
				uncompressedData.write(compressedData) #uncompressed
			else:
				
				uncompressedData.write(decompress(compressionType, compressedData, uncompressedSize))
				
			compressedDataStart += compressedSize+4
			print '\tDecompressing Part 1: Completed Section '+str(m+1)+' of '+str(compBlockCount)
			
		if LE2BE(rawDataChunk, compressedDataStart, 8) == '1004fa9957fbaa33':
			header2Start = compressedDataStart
			compressionType = LE2DEC(rawDataChunk, header2Start+10, 1)
			compBlockCount = LE2DEC(rawDataChunk, header2Start+15, 4)
			compressedDataStart = header2Start+19+compBlockCount*4
			for m in xrange(compBlockCount):
				uncompressedSize = LE2DEC(rawDataChunk, header2Start+19+m*4, 2)
				compressedSize = LE2DEC(rawDataChunk, header2Start+21+m*4, 2)
				compressedData = BE(rawDataChunk, compressedDataStart+4, compressedSize)
				if uncompressedSize == compressedSize:
					uncompressedData.write(compressedData) #uncompressed
				else:
					uncompressedData.write(decompress(compressionType, compressedData, uncompressedSize))
				compressedDataStart += compressedSize+4
				print '\tDecompressing Part 2: Completed Section '+str(m+1)+' of '+str(compBlockCount)
		else:
			raise Exception('Compression Issue')
	else:
		if binascii.unhexlify('33AAFB5799FA0410') in rawDataChunk:
			raise Exception('Compression Issue')
		else:
			uncompressedData.write(rawDataChunk) #if the if statment is not true the file is not compressed
	
	# outFile = open(CONFIG['dumpFolder']+os.sep+forgeFile+os.sep+fileList[x][fileID]['fileName']+'.acu', 'wb')
	# outFile = open(CONFIG['dumpFolder']+os.sep+fileList[x][fileID]['fileName']+'.datafile', 'wb')
	# outFile.write(uncompressedData)
	# outFile.close()
	uncompressedData.close()
	uncompressedData = open(CONFIG['dumpFolder'] + os.sep +'temp' + os.sep +'raw' + os.sep + 'temp', 'rb')
	
	uncompressedData.seek(0)
	fileCount = LE2DEC2(uncompressedData.read(2))
	fileOffset = 2+fileCount*14
	extra16 = 0
	for m in xrange(fileCount):
		uncompressedData.seek(14+m*14+extra16)
		extra16 += 2*LE2DEC2(uncompressedData.read(2))
	fileOffset += extra16
	extra16 = 0
	alphabeticalFiles = {}
	for m in xrange(fileCount):
		uncompressedData.seek(2+m*14+extra16)
		fileID2 = BEHEX2(uncompressedData.read(8)).upper()
		uncompressedData.seek(10+m*14+extra16)
		fileDataSize = LE2DEC2(uncompressedData.read(4)) #(size of file with header)
		uncompressedData.seek(14+m*14+extra16)
		extra16 += 2*LE2DEC2(uncompressedData.read(2))
		uncompressedData.seek(fileOffset)
		resourceType = LE2BE2(uncompressedData.read(4))
		uncompressedData.seek(fileOffset+4)
		fileSize = LE2DEC2(uncompressedData.read(4))+1 #(size of file without header)
		uncompressedData.seek(fileOffset+8)
		fileNameSize = LE2DEC2(uncompressedData.read(4))
		uncompressedData.seek(fileOffset+12)
		fileName = uncompressedData.read(fileNameSize)
		uncompressedData.seek(fileOffset+12+fileNameSize)
		tempFile = uncompressedData.read(fileSize)
		fileType = LE2BE(tempFile, 10, 4).upper()
		# if not os.path.exists(CONFIG['dumpFolder']+os.sep+forgeFile+os.sep+fileList[x][fileID]['fileName']):
			# os.makedirs(CONFIG['dumpFolder']+os.sep+forgeFile+os.sep+fileList[x][fileID]['fileName'])
		# if not os.path.exists(CONFIG['dumpFolder']+os.sep+forgeFile+os.sep+fileList[x][fileID]['fileName']+os.sep+fileType):
			# os.makedirs(CONFIG['dumpFolder']+os.sep+forgeFile+os.sep+fileList[x][fileID]['fileName']+os.sep+fileType)
		if os.path.isfile(CONFIG['dumpFolder']+os.sep+'temp'+os.sep+forgeFile+os.sep+fileList[forgeFile][fileID]['fileName']+os.sep+fileType+os.sep+fileName+'.acu'):
			duplicate = 1
			while os.path.isfile(CONFIG['dumpFolder']+os.sep+'temp'+os.sep+forgeFile+os.sep+fileList[forgeFile][fileID]['fileName']+os.sep+fileType+os.sep+fileName+'_'+str(duplicate)+'.acu'):
				duplicate += 1
			dir = CONFIG['dumpFolder']+os.sep+'temp'+os.sep+forgeFile+os.sep+fileList[forgeFile][fileID]['fileName']+os.sep+fileType+os.sep+fileName+'_'+str(duplicate)+'.acu'
		else:
			dir = CONFIG['dumpFolder']+os.sep+'temp'+os.sep+forgeFile+os.sep+fileList[forgeFile][fileID]['fileName']+os.sep+fileType+os.sep+fileName+'.acu'
		if not os.path.isdir(os.sep.join(dir.split(os.sep)[:-1])):
			os.makedirs(os.sep.join(dir.split(os.sep)[:-1]))

		tempFiles.write(fileID2, {'game': 'ACU', 'forgeFile':forgeFile, 'containerFileID':fileID, 'resourceType':fileType, 'fileName': fileName, 'dir':dir})
		
		if fileName not in alphabeticalFiles:
			alphabeticalFiles[fileName] = []
		alphabeticalFiles[fileName].append(fileID2)
		
		try:
			outFile = open(dir, 'wb')
			outFile.write(tempFile)
			outFile.close()
		except:	
			print 'error saving temporary file'

		fileOffset += fileDataSize
	
	for fileName in sorted([m for m in alphabeticalFiles]):
		for fileID2 in alphabeticalFiles[fileName]:
			fileTree.insert('ACU|'+forgeFile+'|'+fileID, 'end', 'ACU|'+forgeFile+'|'+fileID+'|'+fileID2.upper(), text=fileName)
