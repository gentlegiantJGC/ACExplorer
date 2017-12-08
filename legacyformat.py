import binascii
import json
fileTypes = json.load(open(r".\ACExplorer\ACUnity\fileFormats.json"))

def printFileTypes(fPath):
	f = open(fPath,'rb').read()
	for fileType in fileTypes:
		if binascii.unhexlify(fileType) in f:
			print '{}:{}'.format(fileType,fileTypes[fileType])
			
def nppformat(fPath):
	f = open(fPath,'rb').read()
	l = []
	for fileType in fileTypes:
		if binascii.unhexlify(fileType) in f:
			l.append(fileType[0:2]+' '+fileType[2:4]+' '+fileType[4:6]+' '+fileType[6:8])
	print '|'.join(l)