import os
import struct
import binascii
from ACExplorer.misc import log

def readForge(fileTree, folder):
	fileList = {}
	for forgeFileName in os.listdir(folder):
		if forgeFileName.endswith('.forge'):
			log.info(__name__, 'Building file tree for {}'.format(forgeFileName))
			fileTree.insert('ACU', 'end', 'ACU|{}'.format(forgeFileName), text=forgeFileName)
			f = open(os.path.join(folder, forgeFileName), 'rb')
			# header
			if f.read(8) != 'scimitar':
				continue
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
			indexTable = struct.unpack('<'+'q8si'*indexCount, f.read(20*indexCount))
			f.seek(nameTableOffset)
			nameTable = struct.unpack('<'+'i40x128s20x'*indexCount, f.read(192*indexCount))
			forgeDatafiles = {}
			for n in xrange(indexCount):
				fileID = binascii.hexlify(indexTable[n*3+1]).upper()
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
					fileTree.insert('ACU|{}'.format(forgeFileName), 'end', 'ACU|{}|{}'.format(forgeFileName, fileID), text=fileName)
			f.close()
	return fileList