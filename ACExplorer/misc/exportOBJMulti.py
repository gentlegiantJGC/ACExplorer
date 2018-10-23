import os
import json
# from ACExplorer.ACUnity import decompressDatafile
from ACExplorer.ACUnity.exportTexture_ import export_texture
from ACExplorer.ACUnity.getMaterialIDs_ import getMaterialIDs
from ACExplorer.ACUnity.readModel_ import readModel
# from ACExplorer.misc import tempFiles

def transform(transformationMtx, vertex):
	# Transformation Matrix transformationMtx[0-3][0-3]
	# [M11 M12 M13 M14][x]
	# |M21 M22 M23 M24||y|
	# |M31 M32 M33 M34||z|
	# [M41 M42 M43 M44][1]
	vertex += [1]
	newVertex = [0,0,0,0]
	
	for m in range(4):
		for n in range(4):
			newVertex[m] += transformationMtx[m][n] * vertex[n]
	return newVertex[0:3]


def exportOBJMulti(app, rootID, fileIDList):
	print fileIDList
	#fileIDList format
	# [
	# {'fileID':'0000000000000000', 'transformationMtx': },
	# {'fileID':'0000000000000000', 'transformationMtx': },
	# {'fileID':'0000000000000000', 'transformationMtx': }
	# ]
	
	# fileIDList format V2
	# {
	# '0000000000000000' : [{'tm':[<transformationMtx1.1>, <transformationMtx1.2>, ...],'BB':[]}, {'tm':[<transformationMtx2.1>, <transformationMtx2.2>, ...],'BB':[]}, ...],
	# '0000000000000000' : [{'tm':[<transformationMtx1.1>, <transformationMtx1.2>, ...],'BB':[]}, {'tm':[<transformationMtx2.1>, <transformationMtx2.2>, ...],'BB':[]}, ...],
	# ...
	# }
	
	if not tempFiles.exists(rootID):
		app.gameFunctions.decompressDatafile(app, rootID)
	rootData = tempFiles.read(rootID)
	if len(rootData) == 0:
		raise Exception('file {} is empty'.format(rootID))
	rootData = rootData[0]
	
	# remove models that couldn't be read
	meshCount = 0
	ticker = 0
	failedModels = []
	for fileID in fileIDList:
		
		if not tempFiles.exists(fileID):
			app.gameFunctions.decompressDatafile(app, fileID)
		data = tempFiles.read(fileID)
		if len(data) == 0:
			raise Exception('file {} is empty'.format(fileID))
		data = data[0]
		
		if not os.path.isfile(data['dir'].replace('.acu', '.json')):
			try:
				readModel(app, fileID)
			except:
				print 'Failed reading model {}'.format(data['fileName'])
		if os.path.isfile(data['dir'].replace('.acu', '.json')):
			meshCount += len(fileIDList[fileID])
			ticker += 1
			print 'read model {} of {}'.format(ticker, len(fileIDList))
		else:
			failedModels.append(fileID)
	for fileID in failedModels:
		del fileIDList[fileID]
	
	rootID = rootID.upper()
	fileName = rootData['fileName']
	savePath = os.path.join(app.CONFIG['dumpFolder'], fileName)
	# savePath = path[:-4] + ".obj"
	# str1 = os.sep.join(savePath.split(os.sep)[:-1])	#save path folder
	# while (treeNode1.Parent != null)
		# treeNode1 = treeNode1.Parent;
	# string str2 = treeNode1.Tag.ToString().ToLower();					'acu'
	
	# obj file
	fio = open(savePath + ".obj", 'w')																		# open obj
	fio.write("# Wavefront Object File\n")														# write text
	fio.write("# Exported by ACExplorer based on code from ARchive_neXt\n")
	fio.write("mtllib " + fileName + ".mtl\n")
	fio.write('\n')
	offset = 0
	tempFileRepeat = {}
	
	# mtl file
	fim = open(savePath + ".mtl", 'w')
	fim.write("# Material Library\n")
	fim.write("# Exported by ACExplorer based on code from ARchive_neXt\n")
	fim.write("\n")
	idsAdded = []
	missingNo = False
	meshNo = 0
	
	for index0, fileID in enumerate(fileIDList):

		if not tempFiles.exists(fileID):
			app.gameFunctions.decompressDatafile(app, fileID)
		data = tempFiles.read(fileID)
		if len(data) == 0:
			raise Exception('file {} is empty'.format(fileID))
		data = data[0]
		
		# used in face data section to define unique names
		if fileID not in tempFileRepeat:
			tempFileRepeat[fileID] = 0
		else:
			tempFileRepeat[fileID] += 1
		
		with open(data['dir'].replace('.acu', '.json')) as f:
			try:
				model = json.loads(f.read())
			except:
				print data['fileName']
				raise Exception()
			#num2 = model['modelScale']# * 0.0002 * 10 * 0.2	# model scale
			num3 = 2048.0
			num4 = 0
			# if model['typeSwitch'] != 3:
				# num2 = 100.0
			# else:
				# num2 = 0.00305
				# num2 = 1
			
			# vertex data
			
			# Transformation Matrix fileContainer['tm'][0-3][0-3]
			# [M11 M12 M13 M14][x]
			# |M21 M22 M23 M24||y|
			# |M31 M32 M33 M34||z|
			# [M41 M42 M43 M44][1]
			for fileContainer in fileIDList[fileID]:
				meshNo += 1
				for vertex in model['vertData']['vertex']:
					vertex = [vertex['X'], vertex['Y'], vertex['Z']]
					for tm in reversed(fileContainer['tm']):
						vertex = transform(tm, vertex)
					fio.write("v " +
					str(round(vertex[0], 6))
					
					+ " " +
					
					str(round(vertex[1], 6))
					
					+ " " +
					
					str(round(vertex[2], 6))
					
					+ '\n')
				print 'written vertex data {} of {}'.format(meshNo, meshCount)
				
				# texture coordinates
				for tVert in model['vertData']['tVert']:
					fio.write('vt {} {}\n'.format(round((tVert['X'] / num3), 6), round((tVert['Y'] / -num3), 6)))
				print 'written texture coordinates {} of {}'.format(meshNo, meshCount)
				
				# face mappings
				for index1, meshData in enumerate(model['meshData']):
					num5 = meshData['vertCount']		#vertex number?
					num6 = meshData['vertStart'] / 3
					if model['typeSwitch'] == 0 and model['faceCount'] != model['facesUsed']:
						if index1 > 0:
							num6 = num4 * 64
							num4 += model['meshFaceBlocks'][index1]
						else:
							num4 = model['meshFaceBlocks'][index1]
					fio.write("g " + data['fileName'] + "_" + str(tempFileRepeat[fileID]) + '_' +str(index1) + '\n')
					
					textureIDs = getMaterialIDs(app, model['materialId'][index1])
					
					if textureIDs == None:
						fio.write("usemtl missingNo\n")
					else:
						for hexid in textureIDs:
							export_texture(app, textureIDs[hexid])
						data2 = tempFiles.read(model['materialId'][index1].upper())
						if len(data2) == 0:
							raise Exception('file {} is empty'.format(model['materialId'][index1].upper()))
						data2 = data2[0]
						material = data2['fileName']
						fio.write("usemtl " + material + '\n')
					fio.write("s 0\n")
					if model['typeSwitch'] != 3:
						num7 = meshData['X']
					else:
						num7 = 0
					for index2 in range(num6, num5 + num6):
						fio.write("f " + 
							str(int(model['faceData'][index2]['Y'] + 1.0 + num7 + offset)) + "/" + 
							str(int(model['faceData'][index2]['Y'] + 1.0 + num7 + offset)) + " " + 
							str(int(model['faceData'][index2]['X'] + 1.0 + num7 + offset)) + "/" + 
							str(int(model['faceData'][index2]['X'] + 1.0 + num7 + offset)) + " " + 
							str(int(model['faceData'][index2]['Z'] + 1.0 + num7 + offset)) + "/" + 
							str(int(model['faceData'][index2]['Z'] + 1.0 + num7 + offset)) + '\n')
					fio.write("# " + str(num5) + " triangles\n\n")
				offset += len(model['vertData']['vertex'])
				print 'written triangle data {} of {}'.format(meshNo, meshCount)
			
			# material data in mtl
			for materialId in model['materialId']:
				if materialId in idsAdded:
					continue
				else:
					idsAdded.append(materialId)
					
				data2 = tempFiles.read(materialId.upper())
				if len(data2) == 0:
					raise Exception('file {} is emtpy'.format(materialId.upper()))
				data2 = data2[0]
				
				material = data2['fileName']
				if material != "NULL":
					textureIDs = getMaterialIDs(app, materialId)
					
					if textureIDs == None:
						missingNo = True
						continue
					fim.write("newmtl " + material + '\n')
					fim.write("Ka 1.000 1.000 1.000\n")
					fim.write("Kd 1.000 1.000 1.000\n")
					fim.write("Ks 0.000 0.000 0.000\n")
					fim.write("Ns 0.000\n")
					for texType in textureIDs:
						if texType == 'diffuse':
							fim.write("map_Kd ")
						elif texType == 'normal':
							fim.write("bump -bm 0.300 ")
						elif texType == 'specular':
							fim.write("map_Ks ")
						else:
							continue
							
						data3 = tempFiles.read(textureIDs[texType].upper())
						if len(data3) == 0:
							raise Exception('file '+textureIDs[texType].upper()+' is empty')
						data3 = data3[0]
				
						fim.write('{}.dds\n'.format(data3['fileName']))
						if texType == 'diffuse':
							fim.write('map_d {}.dds\n'.format(data3['fileName']))

					fim.write('\n')
			print 'written material data {} of {}'.format(index0, len(fileIDList))
	
	fio.close()
		
	# write misingNo texture if used
	if missingNo:
		fim.write("newmtl missingNo\n")
		fim.write("Ka 1.000 1.000 1.000\n")
		fim.write("Kd 1.000 1.000 1.000\n")
		fim.write("Ks 0.000 0.000 0.000\n")
		fim.write("Ns 0.000\n")
		fim.write("map_Kd missingNo.png\n")
		fim.write('\n')
	fim.close()
	
	print 'Done'
