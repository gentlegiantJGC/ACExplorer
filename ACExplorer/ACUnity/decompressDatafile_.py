import os
import struct
from ACExplorer.misc.dataTypes import BE, BEHEX2, LE2BE, LE2BE2, LE2DEC, LE2DEC2

def decompressDatafile(app, fileID, forgeFile=None):
	if fileID == 0 or fileID > 2**40:
		return
	uncompressedDataList = []
	f = open(os.path.join(app.CONFIG.gameFolder(app.gameFunctions.gameIdentifier), forgeFile), 'rb')
	f.seek(app.fileList[forgeFile][fileID]['rawDataOffset'])
	rawDataChunk = f.read(app.fileList[forgeFile][fileID]['rawDataSize'])
	f.close()
	compBlockCount = 0
	if LE2BE(rawDataChunk, 0, 8) == '1004FA9957FBAA33': # if compressed
		compressionType = LE2DEC(rawDataChunk, 10, 1)
		compBlockCount = LE2DEC(rawDataChunk, 15, 4)
		compressedDataStart = 19+compBlockCount*4
		for m in xrange(compBlockCount):
			uncompressedSize = LE2DEC(rawDataChunk, 19+m*4, 2)
			compressedSize = LE2DEC(rawDataChunk, 21+m*4, 2)
			compressedData = BE(rawDataChunk, compressedDataStart+4, compressedSize)
			uncompressedDataList.append(app.misc.decompress(compressionType, compressedData, uncompressedSize))
				
			compressedDataStart += compressedSize+4
			# print '\tDecompressing Part 1: Completed Section {} of {}'.format(m+1, compBlockCount)
			
		if LE2BE(rawDataChunk, compressedDataStart, 8) == '1004FA9957FBAA33':
			header2Start = compressedDataStart
			compressionType = LE2DEC(rawDataChunk, header2Start+10, 1)
			compBlockCount = LE2DEC(rawDataChunk, header2Start+15, 4)
			compressedDataStart = header2Start+19+compBlockCount*4
			for m in xrange(compBlockCount):
				uncompressedSize = LE2DEC(rawDataChunk, header2Start+19+m*4, 2)
				compressedSize = LE2DEC(rawDataChunk, header2Start+21+m*4, 2)
				compressedData = BE(rawDataChunk, compressedDataStart+4, compressedSize)
				uncompressedDataList.append(app.misc.decompress(compressionType, compressedData, uncompressedSize))
				compressedDataStart += compressedSize+4
				# print '\tDecompressing Part 2: Completed Section {} of {}'.format(m+1, compBlockCount)
		else:
			raise Exception('Compression Issue')
	elif '\x33\xAA\xFB\x57\x99\xFA\x04\x10' in rawDataChunk:
		raise Exception('Compression Issue')
	else:
		uncompressedDataList.append(rawDataChunk) #if the if statment is not true the file is not compressed

	uncompressedData = app.misc.fileObject()
	uncompressedData.write(''.join(uncompressedDataList))

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
		fileID2 = uncompressedData.read(8)
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
		if fileName == '':
			fileName = LE2BE2(fileID2)
		uncompressedData.seek(fileOffset+12+fileNameSize)
		tempFile = uncompressedData.read(fileSize)
		fileType = struct.unpack('<I', tempFile[10:14])[0]
		fileTypeStr = LE2BE(tempFile, 10, 4).upper()
		app.tempNewFiles.add(struct.unpack('<Q', fileID2)[0], forgeFile, fileID, fileType, fileName, rawFile=tempFile)
		if fileName not in alphabeticalFiles:
			alphabeticalFiles[fileName] = []
		alphabeticalFiles[fileName].append(struct.unpack('<Q', fileID2)[0])
		if app.CONFIG['writeToDisk']:
			folder = os.path.join(app.CONFIG['dumpFolder'], 'temp', forgeFile, app.fileList[forgeFile][fileID]['fileName'], fileTypeStr)
			if os.path.isfile(os.path.join(folder, '{}.acu'.format(fileName))):
				duplicate = 1
				while os.path.isfile(os.path.join(folder, '{}_{}.acu'.format(fileName, duplicate))):
					duplicate += 1
				dir = os.path.join(folder, '{}_{}.acu'.format(fileName, duplicate))
			else:
				dir = os.path.join(folder, fileName + '.acu')
			if not os.path.isdir(folder):
				os.makedirs(folder)
			try:
				open(dir, 'wb').write(tempFile)
			except:
				print 'error saving temporary file with path "{}"'.format(dir)
		fileOffset += fileDataSize
	
	for fileName in sorted(alphabeticalFiles, key=lambda v: v.lower()):
		for fileID2 in alphabeticalFiles[fileName]:
			app.fileTree.insert('{}|{}|{}'.format(app.gameFunctions.gameIdentifier, forgeFile, fileID), 'end', '{}|{}|{}|{}'.format(app.gameFunctions.gameIdentifier, forgeFile, fileID, fileID2), text=fileName)
