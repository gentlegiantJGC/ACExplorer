import os
import json
# from ACExplorer.ACUnity import decompressDatafile
from ACExplorer.ACUnity.exportTexture_ import export_texture
from ACExplorer.ACUnity.getMaterialIDs_ import getMaterialIDs
# from ACExplorer.misc import tempFiles


def exportOBJ(app, fileID):
	# if not tempFiles.exists(fileID):
	# 	# TODO fileID is a int value
	# 	decompressDatafile(app, fileID)
	# data = tempFiles.read(fileID)
	# if len(data) == 0:
	# 	raise Exception('file {} is empty'.format(fileID))
	# data = data[0]

	data = app.tempNewFiles.getData(fileID)
	if data is None:
		app.log.warn(__name__, "Failed to find file {}".format(fileID))
		return

	fileName = data['fileName']
	with open(os.path.join(app.CONFIG["dumpFolder"], "temp", data['fileName'])) as f:
		model = json.loads(f.read())
	savePath = os.path.join(app.CONFIG['dumpFolder'], fileName)
	# savePath = path[:-4] + ".obj"
	str1 = os.sep.join(savePath.split(os.sep)[:-1])	#save path folder
	# while (treeNode1.Parent != null)
		# treeNode1 = treeNode1.Parent;
	# if model['typeSwitch'] != 3:
		# num2 = 100.0
	# else:
		# num2 = 0.00305
	# string str2 = treeNode1.Tag.ToString().ToLower();					'acu'
	fio = open(savePath + ".obj", 'w')						# open obj
	fio.write("#Wavefront Object File\n")														# write text
	fio.write("#Exported by gentlegiantJGC based on code from ARchive_neXt\n")
	if len(model['materialId']) > 0:
		fio.write("mtllib " + fileName + ".mtl\n")
	fio.write('\n')
	for vertex in model['vertData']['vertex']:
		fio.write("v " + str(round((vertex['X'] * model['modelScale']), 6)) + " " + str(round((vertex['Y'] * model['modelScale']), 6)) + " " + str(round((vertex['Z'] * model['modelScale']), 6)) + '\n')
	fio.write("# " + str(len(model['vertData']['vertex'])) + " vertices\n")
	fio.write('\n')
	num3 = 2048.0
	for tVert in model['vertData']['tVert']:
		fio.write("vt " + str(round((tVert['X'] / num3), 6)) + " " + str(round((tVert['Y'] / -num3), 6)) + '\n')
	fio.write("# " + str(len(model['vertData']['tVert'])) + " texture coordinates\n")
	fio.write('\n')
	num4 = 0
	for index1, meshData in enumerate(model['meshData']):
		vert_count = meshData['vertCount']		#vertex number?
		num6 = meshData['vertStart'] / 3
		# facesUsed = number of faces in the face table
		# faceCOunt = sum of mesh table face count
		if model['typeSwitch'] == 0 and model['faceCount'] != model['facesUsed']:
			if index1 > 0:
				num6 = num4 * 64
				num4 += model['meshFaceBlocks'][index1]
			else:
				num4 = model['meshFaceBlocks'][index1]
		fio.write("g " + fileName + "_" + str(index1) + '\n')
		
		
		
		
		textureIDs = getMaterialIDs(app, model['materialId'][index1])
		if textureIDs == None:
			fio.write("usemtl missingNo\n")
		# print textureIDs
		else:
			for hexid in textureIDs:
				# textureFile = getFile(workingDir, textureIDs[hexid])
				export_texture(app, textureIDs[hexid])
			material = app.tempNewFiles.getData(model['materialId'][index1])['fileName']
			fio.write("usemtl " + material + '\n')
		fio.write("s 0\n")
		if model['typeSwitch'] != 3:
			num7 = meshData['X']
		else:
			num7 = 0
		for index2 in range(num6, vert_count + num6):
			fio.write("f " + 
				str(int(model['faceData'][index2]['Y'] + 1.0 + num7)) + "/" + 
				str(int(model['faceData'][index2]['Y'] + 1.0 + num7)) + " " + 
				str(int(model['faceData'][index2]['X'] + 1.0 + num7)) + "/" + 
				str(int(model['faceData'][index2]['X'] + 1.0 + num7)) + " " + 
				str(int(model['faceData'][index2]['Z'] + 1.0 + num7)) + "/" + 
				str(int(model['faceData'][index2]['Z'] + 1.0 + num7)) + '\n')
		fio.write("# " + str(vert_count) + " triangles\n\n")
	fio.close()
		
	if len(model['materialId']) > 0:
		fim = open(savePath + ".mtl", 'w')
		fim.write("# Material Library\n")
		fim.write("# Exported by code based on ARchive_neXt\n")
		fim.write("\n")
		idsAdded = []
		for materialId in model['materialId']:
			if materialId in idsAdded:
				continue
			else:
				idsAdded.append(materialId)
			material = app.tempNewFiles.getData(materialId)['fileName']
			if material is not None:
				textureIDs = getMaterialIDs(app, materialId)
				if textureIDs is None:
					fim.write("newmtl missingNo\n")
				else:
					fim.write("newmtl " + material + '\n')
				fim.write("Ka 1.000 1.000 1.000\n")
				fim.write("Kd 1.000 1.000 1.000\n")
				fim.write("Ks 0.000 0.000 0.000\n")
				fim.write("Ns 0.000\n")
				if textureIDs == None:
					fim.write("map_Kd " + app.CONFIG["missingNo"] + "\n")
				else:
					for texType in textureIDs:
						if texType == 'diffuse':
							fim.write("map_Kd ")
						elif texType == 'normal':
							fim.write("bump -bm 0.300 ")
						elif texType == 'specular':
							fim.write("map_Ks ")
						else:
							continue
						fim.write(app.tempNewFiles.getData(int(textureIDs[texType], 16))['fileName'] + '.dds\n')
						if texType == 'diffuse':
							fim.write("map_d ")
							fim.write(app.tempNewFiles.getData(int(textureIDs[texType], 16))['fileName'] + '.dds\n')

				fim.write('\n')
		fim.close()
	
	print 'done'
