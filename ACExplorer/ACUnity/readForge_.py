import os
import struct

def readForge(app, folder):
	fileList = {}
	for forgeFileName in os.listdir(folder):
		if forgeFileName.endswith('.forge'):
			app.log.info(__name__, 'Building file tree for {}'.format(forgeFileName))
			f = open(os.path.join(folder, forgeFileName), 'rb')
			# header
			if f.read(8) != 'scimitar':
				continue
			app.fileTree.insert('ACU', 'end', 'ACU|{}'.format(forgeFileName), text=forgeFileName)
			fileList[forgeFileName] = {}
			f.seek(1, 1)
			forgeFileVersion, fileDataHeaderOffset = struct.unpack('<iQ', f.read(12))
			if forgeFileVersion != 27:
				raise Exception('Unsupported Forge file format : "{}"'.format(forgeFileVersion))
			f.seek(fileDataHeaderOffset+36)
			fileDataOffset = struct.unpack('<q', f.read(8))[0]
			f.seek(fileDataOffset)
			# File Data
			indexCount, indexTableOffset, fileDataOffset2, nameTableOffset, rawDataTableOffset = struct.unpack('<i4x2q8x2q', f.read(48))
			f.seek(indexTableOffset)
			indexTable = struct.unpack('<'+'QQI'*indexCount, f.read(20*indexCount))
			f.seek(nameTableOffset)
			nameTable = struct.unpack('<'+'i40x128s20x'*indexCount, f.read(192*indexCount))
			forgeDatafiles = {}
			for n in xrange(indexCount):
				fileID = indexTable[n*3+1]
				fileName = nameTable[n*2+1].replace('\x00', '')
				if indexTable[n*3+2] != nameTable[n*2]:
					raise Exception('These should be the same. Is something wrong?')
				fileList[forgeFileName][fileID] = {  # file data id (matches the id in the file)
					'rawDataOffset': indexTable[n*3],
					'rawDataSize': indexTable[n*3+2],
					'fileName': fileName
				}

				if fileName not in forgeDatafiles:
					forgeDatafiles[fileName] = []
				forgeDatafiles[fileName].append(fileID)

			for fileName in sorted(forgeDatafiles, key=lambda v: v.lower()):
				for fileID in forgeDatafiles[fileName]:
					app.fileTree.insert('{}|{}'.format(app.gameFunctions.gameIdentifier, forgeFileName), 'end', '{}|{}|{}'.format(app.gameFunctions.gameIdentifier, forgeFileName, fileID), text=fileName)
			f.close()
	return fileList