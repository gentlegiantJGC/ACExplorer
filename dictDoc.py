# import json
#
# dictDoc = {}
#
# with open(r"D:\Unity_Dump\Dictionary\dictionaryDoc.txt") as f:
# 	for line in f.readlines():
# 		if ':::::' not in line:
# 			continue
# 		fileID, j = line.replace('\n', '').split(':::::')
# 		fileID = ' '.join([fileID[n:n+2] for n in range(0, 16, 2)])
# 		j = eval(j)
# 		try:
# 			dictDoc[fileID] = '|'.join([' '.join([i[n:n+2] for n in range(0, 16, 2)]) for i in j[1][0][5]])
# 		except:
# 			continue
#
# with open(r"D:\Unity_Dump\Dictionary\dictionaryDocIDSearch.txt", 'w') as f:
# 	for fileID in dictDoc:
# 		f.write('{}:::::{}\n'.format(fileID, dictDoc[fileID]))

from ACExplorer.misc.decompress_ import decompress
import time

a = open(r'D:\Unity_Dump\ACModels\temp\32768.1', 'rb').read()
aOut = open(r'D:\Unity_Dump\ACModels\temp\32768.1.out', 'rb').read()
# b = open(r'D:\Unity_Dump\ACModels\temp\32768.2', 'rb').read()
# print len(a)
# print len(b)
t = time.time()
for _ in xrange(1000000):
	decompressedAB = decompress(1, a, 32768)
print time.time() - t

# print decompressedAB == aOut
# decompressedA = decompress(1, a, 32768)
# decompressedB = decompress(1, b, 32768)
# print len(decompressedA)
# print len(decompressedB)

# open(r'D:\Unity_Dump\ACModels\temp\32768.1.out', 'wb').write(decompressedA)
# open(r'D:\Unity_Dump\ACModels\temp\32768.2.out', 'wb').write(decompressedB)
# open(r'D:\Unity_Dump\ACModels\temp\32768.12.outx2', 'wb').write(decompressedAB)

print 'done'