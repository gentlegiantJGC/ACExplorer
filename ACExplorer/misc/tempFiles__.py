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
import json, os
from ACExplorer import CONFIG

tempFileContainer = {}

path = '{0}{1}temp{1}tempFiles{1}ACU'.format(CONFIG['dumpFolder'],os.sep)
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
	if not os.path.isdir('{0}{1}temp{1}tempFiles'.format(CONFIG['dumpFolder'],os.sep)):
		os.makedirs('{0}{1}temp{1}tempFiles'.format(CONFIG['dumpFolder'],os.sep))
	# write tempFilesFile
	tempFilesFile = open('{0}{1}temp{1}tempFiles{1}ACU'.format(CONFIG['dumpFolder'],os.sep), 'w')
	tempFilesFile.write(json.dumps(tempFileContainer))
	tempFilesFile.close()
	
def exists(fileID):
	return len(read(fileID)) > 0
					
def populateTree(app):
	folderLen = len(tempFileContainer)
	ticker = 1
	tempFileTree = {}
	for fileID in tempFileContainer:
		tempFile = read(fileID)
		for data in tempFile:
			key = '{}|{}|{}'.format(data['game'], data['forgeFile'], data['containerFileID'])
			if key not in tempFileTree:
				tempFileTree[key] = {}
			if data['fileName'] not in tempFileTree[key]:
				tempFileTree[key][data['fileName']] = []
			tempFileTree[key][data['fileName']].append(fileID)

		if ticker % 100 == 0:
			pass
			# TODO: \/
			# log.info(__name__, 'Populating file tree: {} of {} completed'.format(ticker, folderLen))
		ticker += 1
	for containerFileID in tempFileTree:
		for fileName in sorted(tempFileTree[containerFileID], key=lambda v: v.lower()):
			for fileID2 in tempFileTree[containerFileID][fileName]:
				app.fileTree.insert(containerFileID, 'end', '{}|{}'.format(containerFileID, fileID2), text=fileName)

