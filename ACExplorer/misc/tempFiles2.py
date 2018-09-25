'''
Forge file
Forge1.forge
	dataFile1
		file1
		file2
		...
	dataFile2
		file1
		file2
		...
	dataFile3
		file1
		file2
		...
	...
Forge2.forge
	dataFile1
		file1
		file2
		...
	dataFile2
		file1
		file2
		...
	dataFile3
		file1
		file2
		...
	...
'''

'''
tempFiles
{
	fileID:{
		<forgeFile>:{
			<datafileID>:{
				'fileType':fileType,
				'fileName': fileName,
				'rawFile':None
			},
			<datafileID2>:{
				'fileType':fileType,
				'fileName': fileName,
				'rawFile':None
			}
		},
		<forgeFile2>:{},
		...
	},
	fileID2:{
		<forgeFile>:{},
		...
	},
	...
}
'''

'''
tempFiles
{
	<fileID>:(<forgeFile>, <datafileID>, <fileType>, <fileName>, None),
	...
}
'''

'''
lightDictionary
{
	fileID:{
		<forgeFile>:[]
	}
}
'''

import struct
import binascii

class tempFilesContainer:
	def __init__(self, app):
		self.app = app
		# dictionary to look up which dataFile a fileID is contained in (if it itself is not the main file in the dataFile)
		self.lightDictionary = {}
		self.lightDictChanged = False
		# the amount of memory self.rawFiles takes (used to remove files)
		self.memory = 0
		# a dictionary of every file currently loaded into memory
		self.tempFiles = {}
		self.lastUsed = []

	def add(self, fileID, forgeFile, datafileID, fileType, fileName, rawFile=None):
		'''
		:param fileID: int
		:param forgeFile: str
		:param datafileID: int of containing datafile
		:param fileType: int
		:param fileName: str
		:param rawFile: binary
		:return:
		'''
		if fileID in self.tempFiles:
			self.memory -= len(self.tempFiles[fileID][4])
		self.refreshUsage(fileID)
		self.tempFiles[fileID] = (forgeFile, datafileID, fileType, fileName, rawFile)
		if rawFile is not None:
			self.memory += len(rawFile)

		while self.memory > self.app.CONFIG['tempFilesMaxMemoryMB']*1000000:
			removeEntry = self.lastUsed.pop(0)
			self.memory -= len(self.tempFiles[removeEntry][4])
			del self.tempFiles[removeEntry]

		if fileID != datafileID:
			if str(fileID) not in self.lightDictionary:
				self.lightDictionary[str(fileID)] = {}
			if forgeFile not in self.lightDictionary[str(fileID)]:
				self.lightDictionary[str(fileID)][forgeFile] = []
			if datafileID not in self.lightDictionary[str(fileID)][forgeFile]:
				self.lightDictionary[str(fileID)][forgeFile].append(datafileID)
				self.lightDictChanged = True

	def getData(self, fileID, forgeFile=None, datafileID=None):
		'''
		:param fileID: int
		:param forgeFile: str
		:param datafileID: int of the containing datafile
		:return:
		'''

		'''
		if file exists in tempfiles and meets the criteria then use that
		if not search for it in filelist                    (it is either a top level id or sub level id)
			if it is there decompress it and use that
		'''

		if forgeFile is not None and datafileID is None:
			if fileID in self.tempFiles and forgeFile == self.tempFiles[fileID][0]:
				datafileID = self.tempFiles[fileID][1]
			else:
				# preferentially use one found in the forgeFile asked but look in others if needed
				if forgeFile in self.app.fileList and fileID in self.app.fileList[forgeFile]:
					datafileID = fileID
				elif str(fileID) in self.lightDictionary and forgeFile in self.lightDictionary[str(fileID)]:
					datafileID = self.lightDictionary[str(fileID)][0]
				else:
					forgeFile = None
		if forgeFile is None:
			forgeFile = next((fF for fF in self.app.fileList if fileID in self.app.fileList[fF]), None)
			if forgeFile is None:
				if str(fileID) in self.lightDictionary: # could check the lower down stuff but if this exists there should be data inside
					forgeFile = self.lightDictionary[str(fileID)].keys()[0]
					datafileID = self.lightDictionary[str(fileID)][forgeFile].keys()[0]
			else:
				datafileID = fileID

		if not (fileID in self.tempFiles and forgeFile == self.tempFiles[fileID][0] and datafileID == self.tempFiles[fileID][1]):
			self.app.gameFunctions.decompressDatafile(self.app, datafileID, forgeFile)
		self.refreshUsage(fileID)
		if fileID in self.tempFiles and forgeFile == self.tempFiles[fileID][0] and datafileID == self.tempFiles[fileID][1]:
			return {
				'forgeFile': forgeFile,
				'datafileID': datafileID,
				'fileType': self.tempFiles[fileID][2],
				'fileName': self.tempFiles[fileID][3],
				'rawFile': self.tempFiles[fileID][4]
			}
		else:
			return None



		#
		# if forgeFile is not None:
		# 	if datafileID is not None:
		# 		if fileID in self.tempFiles and self.tempFiles[fileID][0] == forgeFile and self.tempFiles[fileID][1] == datafileID:
		# 			return mergeDict(self.tempFiles[fileID][forgeFile][datafileID], {'forgeFile':forgeFile, 'datafileID':datafileID})
		# 		else:
		# 			raise Exception('Both forgeFile and datafileID were given ("{}" and "{}" respectively) but the data was not there')
		# 	if fileID in self.tempFiles and forgeFile in self.tempFiles[fileID]:
		# 		datafileID = self.tempFiles[fileID][forgeFile].keys()[0]
		# 		return mergeDict(self.tempFiles[fileID][forgeFile][datafileID], {'forgeFile':forgeFile, 'datafileID':datafileID})
		# 	if fileID in self.lightDictionary and forgeFile in self.lightDictionary[fileID]:
		# 		datafileID = self.lightDictionary[fileID][forgeFile][0]
		# 		self.app.gameFunctions.decompressDatafile(self.app, datafileID, forgeFile)
		# 		return mergeDict(self.tempFiles[fileID][forgeFile][datafileID], {'forgeFile':forgeFile, 'datafileID':datafileID})
		# if fileID not in self.tempFiles and fileID in self.lightDictionary:
		# 	forgeFile = self.lightDictionary[fileID].keys()[0]
		# 	datafileID = self.lightDictionary[fileID][forgeFile][0]
		# 	self.app.gameFunctions.decompressDatafile(self.app, datafileID, forgeFile)
		# 	return mergeDict(self.tempFiles[fileID][forgeFile][datafileID], {'forgeFile':forgeFile, 'datafileID':datafileID})
		# if fileID in self.tempFiles:
		# 	forgeFile = self.tempFiles[fileID].keys()[0]
		# 	datafileID = self.tempFiles[fileID][forgeFile].keys()[0]
		# 	return mergeDict(self.tempFiles[fileID][forgeFile][datafileID], {'forgeFile':forgeFile, 'datafileID':datafileID})
		# return None

	def getFile(self, fileID, forgeFile=None, datafileID=None):
		'''
		:param fileID: int
		:param forgeFile: str
		:param datafileID: int
		:return:
		'''
		data = self.getData(fileID, forgeFile, datafileID)
		forgeFile = data['forgeFile']
		datafileID = data['datafileID']
		if data['rawFile'] is None:
			self.app.gameFunctions.decompressDatafile(self.app, datafileID, forgeFile)
		self.refreshUsage(fileID)
		return data['rawFile']

	def clear(self):
		self.lightDictionary.clear()
		self.memory = 0
		self.tempFiles.clear()
		self.lastUsed = []
		self.lightDictChanged = False

	def refreshUsage(self, fileID):
		if fileID in self.tempFiles:
			self.lastUsed.remove(fileID)
		self.lastUsed.append(fileID)

def mergeDict(a,b):
	c = a.copy()
	c.update(b)
	return c