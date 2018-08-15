import os
from ACExplorer.misc import log
from ACExplorer.misc.dataTypes import BE, BEHEX, LE2DEC


def readForge(fileTree, folder):
	fileList = {}
	for x in os.listdir(folder):
		if x.endswith('.forge'):
			log.info(__name__, 'Building file tree for {}'.format(x))
			fileTree.insert('ACU', 'end', 'ACU|'+x, text=x)
			f = open(folder+os.sep+x, 'rb')
			fileLocation = 0
			ftemp = f.read(21)
			fileLocation += 21
			if ftemp[0:8] != "scimitar":
				continue
			fileList[x] = {}
			fileDataHeaderOffset = LE2DEC(ftemp, 13, 8) #read the offset to File Data Header, LE -> BE, hex, dec
			f.read(fileDataHeaderOffset-21)
			fileLocation += fileDataHeaderOffset-21
			ftemp = f.read(44)
			fileLocation += 44
			fileDataOffset = LE2DEC(ftemp, 36, 8)
			f.read(fileDataOffset-fileLocation)
			fileLocation += fileDataOffset-fileLocation
			ftemp = f.read(48)
			fileLocation += 48
			indexCount = LE2DEC(ftemp, 0, 4)
			indexTableOffset = LE2DEC(ftemp, 8, 8)
			nameTableOffset = LE2DEC(ftemp, 32, 8)
			
			f.read(indexTableOffset-fileLocation)
			fileLocation += indexTableOffset-fileLocation
			indexTable = f.read(indexCount*20)
			fileLocation += indexCount*20
			
			f.read(nameTableOffset-fileLocation)
			fileLocation += nameTableOffset-fileLocation
			nameTable = f.read(indexCount*192)
			fileLocation += indexCount*192
			forgeDatafiles = {}
			for n in xrange(1, indexCount-1):
				fileID = BEHEX(indexTable, 8+n*20, 8).upper()
				fileList[x][fileID] = {					#file data id (matches the id in the file)
					'rawDataOffset'	: LE2DEC(indexTable, n*20, 8),
					'rawDataSize'	: LE2DEC(indexTable, 16+n*20, 4),
					'fileName'	: BE(nameTable, n*192+44, 128).replace('\x00', '')			#file name
				}
				
				if fileList[x][fileID]['fileName'] not in forgeDatafiles:
					forgeDatafiles[fileList[x][fileID]['fileName']] = []
				forgeDatafiles[fileList[x][fileID]['fileName']].append(fileID)
					
				
				if fileList[x][fileID]['rawDataSize'] != LE2DEC(nameTable, n*192, 4):
					raise Exception('These should be the same. Is something wrong?')
			
			for fileName in sorted(forgeDatafiles, key=lambda v: v.lower()):
				for fileID in forgeDatafiles[fileName]:
					fileTree.insert('ACU|'+x, 'end', 'ACU|'+x+'|'+fileID, text=fileName)
			
			
			
			
			f.close()
	return fileList
