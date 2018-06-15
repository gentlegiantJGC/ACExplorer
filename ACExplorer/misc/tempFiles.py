'''
tempFiles are stored in one json file
fileID - for file name


fileID:[{
'game':
'forgeFile':
'containerFileID':
'resourceType':fileType,
'fileName': fileName,
'dir':dir
}
...
],
fileID2:[
{}
]
...


'''
import json
import os

from ACExplorer import CONFIG
from ACExplorer.misc import log

tempFileContainer = {}

path = CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles' + os.sep + 'ACU'
if os.path.isfile(path):
	with open(path) as tempFilesFile:
		tempFileContainer = json.load(tempFilesFile)
	
def read(fileID):
	if fileID in tempFileContainer:
		tempFile = tempFileContainer[fileID]
	else:
		tempFile = []
	return tempFile
	
def write(fileID, data):
	if fileID not in tempFileContainer:
		tempFileContainer[fileID] = []
	if data not in tempFileContainer[fileID]:
		tempFileContainer[fileID].append(data)

# this function is called once a datafile is fully compressed
def save():
	# if the folder doesn't exist, make it
	if not os.path.isdir(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles'):
		os.makedirs(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles')
	# write tempFilesFile
	tempFilesFile = open(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles' + os.sep + 'ACU', 'w')
	tempFilesFile.write(json.dumps(tempFileContainer))
	tempFilesFile.close()
	
def exists(fileID):
	return len(read(fileID)) > 0
					
def populateTree(fileTree):
	folderLen = len(tempFileContainer)
	ticker = 1
	tempFileTree = {}
	for fileID in tempFileContainer:
		tempFile = read(fileID)
		for data in tempFile:
		
			if data['game']+'|'+data['forgeFile']+'|'+data['containerFileID'] not in tempFileTree:
				tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']] = {}
			if data['fileName'] not in tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']]:
				tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']][data['fileName']] = []
			tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']][data['fileName']].append(fileID)

		if ticker % 100 == 0:
			log.info(__name__, 'Populating file tree: {} of {} completed'.format(ticker, folderLen))
		ticker += 1
	for containerFileID in tempFileTree:
		for fileName in sorted([m for m in tempFileTree[containerFileID]]):
			for fileID2 in tempFileTree[containerFileID][fileName]:
				fileTree.insert(containerFileID, 'end', containerFileID+'|'+fileID2, text=fileName)

