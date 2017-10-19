import binascii
import json
fileTypes = json.load(open(r".\ACExplorer\ACUnity\fileFormats.json"))

def printFileTypes(fPath):
	f = open(fPath,'rb').read()
	for fileType in fileTypes:
		if binascii.unhexlify(fileType) in f:
			print '{}:{}'.format(fileType,fileTypes[fileType])