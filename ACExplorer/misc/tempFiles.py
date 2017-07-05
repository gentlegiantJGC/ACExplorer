'''
tempFiles stored by id in seperate files
fileID - for file name
{
'game':
'forgeFile':
'containerFileID':
'resourceType':fileType,
'fileName': fileName,
'dir':dir
}

'''
import json
import os

from ACExplorer import CONFIG


def read(fileID):
	if os.path.isfile(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles' + os.sep + fileID):
		tempFilesFile = open(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles' + os.sep + fileID)
		tempFile = json.load(tempFilesFile)
		tempFilesFile.close()
	else:
		tempFile = []
	return tempFile

def write(fileID, data):
	# if the folder doesn't exist, make it
	if not os.path.isdir(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles'):
		os.makedirs(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles')
	# if the file exists, read from it
	if os.path.isfile(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles' + os.sep + fileID):
		# read contents of the file
		tempFilesFile = open(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles' + os.sep + fileID)
		tempFile = json.load(tempFilesFile)
		tempFilesFile.close()
	else:
		# if the file doesn't exist make a blank list
		tempFile = []
	# if the data is not in tempFile, add it
	if data not in tempFile:
		tempFile.append(data)
	# write tempFilesFile
	tempFilesFile = open(CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles' + os.sep + fileID, 'w')
	tempFilesFile.write(json.dumps(tempFile))
	tempFilesFile.close()
	
def exists(fileID):
	if len(read(fileID)) > 0:
		return True
	else:
		return False
	
def populateTree(fileTree):
	path = CONFIG['dumpFolder'] + os.sep + 'temp' + os.sep + 'tempFiles'
	if os.path.isdir(path):
		folderLen = len(os.listdir(path))
		ticker = 1
		tempFileTree = {}
		for fileID in os.listdir(path):
			tempFile = read(fileID)
			for data in tempFile:
			
				if data['game']+'|'+data['forgeFile']+'|'+data['containerFileID'] not in tempFileTree:
					tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']] = {}
				if data['fileName'] not in tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']]:
					tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']][data['fileName']] = []
				tempFileTree[data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']][data['fileName']].append(fileID)
				
				# pos = 'end'
				# for tID in fileTree.get_children(data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']):
					# if data['fileName'] < fileTree.item(tID, 'text'):
						# pos = fileTree.index(tID)
						# break
				# fileTree.insert(data['game']+'|'+data['forgeFile']+'|'+data['containerFileID'], pos, data['game']+'|'+data['forgeFile']+'|'+data['containerFileID']+'|'+fileID, text=data['fileName'])

			if ticker % 100 == 0:
				print "Populating file tree: "+str(ticker)+" of "+str(folderLen)+" completed"
			ticker += 1
		for containerFileID in tempFileTree:
			for fileName in sorted([m for m in tempFileTree[containerFileID]]):
				for fileID2 in tempFileTree[containerFileID][fileName]:
					fileTree.insert(containerFileID, 'end', containerFileID+'|'+fileID2, text=fileName)
