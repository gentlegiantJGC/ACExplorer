def exportFakes(fileTree, fileList, config, fileID):
	import binascii
	from misc import tempFiles
	from misc.dataTypes import float32, BEHEX2
	from misc.exportOBJMulti import exportOBJMulti
	if not tempFiles.exists(config, fileID):
		decompressDatafile(fileTree, fileList, config, fileID)
	data = tempFiles.read(config, fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	
	fIn = open(data['dir'], 'rb')
	fReadIn = fIn.read()
	fIn.close()

	files = fReadIn.split(binascii.unhexlify('000000000000000024B57FD7'))[1:]
	
	ticker = 0
	fileIDList = {}
	for n in files:
		if binascii.unhexlify('298D65EC') not in n:
			continue
		if ticker not in fileIDList:
			fileIDList[ticker] = {}
		fileIDList[ticker]['x'] = float32(n[63:67])
		fileIDList[ticker]['y'] = float32(n[67:71])
		fileIDList[ticker]['z'] = float32(n[71:75])
		visualLoc = n.find(binascii.unhexlify('298D65EC'))
		fileIDList[ticker]['id'] = BEHEX2(n[visualLoc+8:visualLoc+16]).upper()
		ticker += 1
	
	exportOBJMulti(fileTree, fileList, config, fileID, fileIDList)