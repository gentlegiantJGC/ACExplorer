import sys, os, json
from ACExplorer.ACUnity.decompressDatafile_ import decompressDatafile
from ACExplorer.ACUnity.formatFile import readID, readStr, readInt, readInt16, readUInt16, readInt32, readUInt32, readFloat32, readType, fOutWrite, ReadRest
from ACExplorer.misc import tempFiles

dev = 'dev' in sys.argv

def readModel(app, fileID):
	if not tempFiles.exists(fileID):
		decompressDatafile(app, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file {} is empty'.format(fileID))
	data = data[0]
	# str1 = strArray[1]			#MDL or HDMDL
	fIn = open(data['dir'], 'rb')				#open parent file
	
	if dev:
		fOut = open(data["dir"]+'.format', 'w')
	else:
		fOut = None
	
	
	
	model = {}
	
	readStr(fIn, fOut, 2)
	# file id
	readID(app, fIn, fOut)
	# file type (should be a model)
	model['fileType'] = readType(fIn, fOut)
	fOutWrite(fOut, '\n')

	readStr(fIn, fOut, 1)		#skip an empty byte
	model['modelType'] = readStr(fIn, fOut, 4)	#
	readStr(fIn, fOut, 1)
	model['aCount'] = readUInt32(fIn, fOut)
	if model['aCount'] > 0:
		raise Exception('aCount not accounted for')
	# {
		# readStr(fIn, fOut, 1)
		# for (int index1 = 0; index1 < 2; ++index1)
		# {
			  # binaryReader.BaseStream.Position += 13L;
			  # if (fi.read(4) > 0)
			  # {
				# int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 1 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
				# return;
			  # }
			  # int num4 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num4 * 4);
			  # int num5 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num5 * 4);
			  # int num6 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num6 * 4);
			  # int num7 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) num7;
			  # int num8 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num8 * 12);
			  # int num9 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num9 * 12);
			  # int num10 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num10 * 12);
			  # int num11 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num11 * 12);
			  # int num12 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num12 * 4);
			  # if (fi.read(4) > 0)
			  # {
				# int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 11 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
				# return;
			  # }
			  # ++binaryReader.BaseStream.Position;
			  # int num13 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num13 * 4);
			  # int num14 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num14 * 2);
			  # int num15 = fi.read(4);
			  # binaryReader.BaseStream.Position += (long) (num15 * 2);
			  # int num16 = fi.read(4);
			  # for (int index2 = 0; index2 < num16; ++index2)
			  # {
				# if (fi.read(4) > 0)
				# {
				  # int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 15 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
				  # return;
				# }
				# if (fi.read(4) > 0)
				# {
				  # int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 16 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
				  # return;
				# }
				# binaryReader.BaseStream.Position += 4L;
				# if (fi.read(4) > 0)
				# {
				  # int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 17 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
				  # return;
				# }
				# ++binaryReader.BaseStream.Position;
				# int num17 = fi.read(4);
				# binaryReader.BaseStream.Position += (long) (num17 * 8);
				# int num18 = fi.read(4);
				# binaryReader.BaseStream.Position += (long) (num18 * 4);
			# }
			# binaryReader.BaseStream.Position += 12L;
		# }
	# }
	model['boneCount'] = readUInt32(fIn, fOut)
	if model['boneCount'] > 0:
		raise Exception('boneCount not accounted for')
	# {
	# arxForm.acModel.boneStruct = new arxForm.acBoneStruct[arxForm.acModel.boneCount];
	# for (int index = 0; index < arxForm.acModel.boneCount; ++index)
	# {
	  # arxForm.acModel.boneStruct[index].boneID = string.Format("{0:X8}", (object) fi.read(8)).PadLeft(16, '0');
	  # arxForm.acModel.boneStruct[index].boneType = string.Format("{0:X4}", (object) fi.read(4)).PadLeft(8, '0');
	  # arxForm.acModel.boneStruct[index].boneName = string.Format("{0:X4}", (object) fi.read(4)).PadLeft(8, '0');
	  # arxForm.acModel.boneStruct[index].transMatrix.M11 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M12 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M13 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M14 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M21 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M22 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M23 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M24 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M31 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M32 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M33 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M34 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M41 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M42 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M43 = binaryReader.ReadSingle();
	  # arxForm.acModel.boneStruct[index].transMatrix.M44 = binaryReader.ReadSingle();
	  # ++binaryReader.BaseStream.Position;
	  # arxForm.acModel.boneStruct[index].transMatrix.Invert();
	# }
	# }
	
	# readStr(fIn, fOut, 41)
	model['boundingBox'] = {}
	model['boundingBox']['minx'] = readFloat32(fIn, fOut)
	model['boundingBox']['miny'] = readFloat32(fIn, fOut)
	model['boundingBox']['minz'] = readFloat32(fIn, fOut)
	readStr(fIn, fOut, 4)
	model['boundingBox']['maxx'] = readFloat32(fIn, fOut)
	model['boundingBox']['maxy'] = readFloat32(fIn, fOut)
	model['boundingBox']['maxz'] = readFloat32(fIn, fOut)
	readStr(fIn, fOut, 4)
	readStr(fIn, fOut, 1)
	# readStr(fIn, fOut, 33) # this may be a bounding box. (float32)
	#First three are all negative followed by a set of zeros
	# Next three three are all positive followed by a set of zeros and a null byte
	readID(app, fIn, fOut)
	if readStr(fIn, fOut, 4).upper() == "FC9E1595":
		readStr(fIn, fOut, 4)
		fOutWrite(fOut, 'Typeswitch\n')
		model['typeSwitch'] = readUInt32(fIn, fOut)
		if model['typeSwitch'] == 0:
			readStr(fIn, fOut, 14)
			fOutWrite(fOut, 'Vert table length\n')
			model['vertTableSize'] = readUInt32(fIn, fOut)
			model['unkLng2'] = readUInt32(fIn, fOut)
			readStr(fIn, fOut, 24)
			model['length1'] = readUInt32(fIn, fOut)
			model['length2'] = readUInt32(fIn, fOut)
			model['meshFaceBlocks'] = []
			model['shadowFaceBlocks'] = []
			fOutWrite(fOut, 'Mesh Face Blocks\n')
			for index in range(model['length1']):
				model['meshFaceBlocks'].append(readUInt32(fIn, fOut))
			for index in range(model['length2']):
				model['shadowFaceBlocks'].append(readUInt32(fIn, fOut))
			model['unkLng'] = readUInt32(fIn, fOut)
			model['unkByt'] = readStr(fIn, fOut, 1)
			fOutWrite(fOut, 'Vert count\n')
			num3 = readUInt32(fIn, fOut)
			model['vertCount'] = num3 / model['vertTableSize']
			model['vertData'] = {}
			model['vertData']['vertex'] = []
			model['vertData']['tVert'] = []
			model['vertData']['normals'] = []
			# arxForm.acModel.vertData = new arxForm.acVertStruct[arxForm.acModel.vertCount];
			fOutWrite(fOut, '\nVert Table\n')
			for index in range(model['vertCount']):
				if model['vertTableSize'] == 48:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Z'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 6)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 4)
					readStr(fIn, fOut, 12)	# bones as below
					# arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.W = (float) binaryReader.ReadByte();
					readStr(fIn, fOut, 4)

				elif model['vertTableSize'] == 40:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Z'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 6)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 12)	# bones as below
					# arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.W = (float) binaryReader.ReadByte();

				elif model['vertTableSize'] == 36:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Z'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 6)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 4)
					readStr(fIn, fOut, 8)	# bones as below
					# arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();

				elif model['vertTableSize'] == 32:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Z'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 6)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 8)	# bones as below
					# arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();

				elif model['vertTableSize'] == 28:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Z'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 6)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 4)

				elif model['vertTableSize'] == 24:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Z'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 6)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))

				elif model['vertTableSize'] == 20:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['normals'][index]['Z'] = float(readInt16(fIn, fOut))
					readStr(fIn, fOut, 2)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))

				elif model['vertTableSize'] == 16:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Y'] = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['Z'] = float(readInt16(fIn, fOut))
					vertScale = float(readInt16(fIn, fOut))
					model['vertData']['vertex'][index]['X'] /= vertScale
					model['vertData']['vertex'][index]['Y'] /= vertScale
					model['vertData']['vertex'][index]['Z'] /= vertScale
					readStr(fIn, fOut, 4)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(readInt16(fIn, fOut))
					model['vertData']['tVert'][index]['Y'] = float(readInt16(fIn, fOut))

				else:
					raise Exception("Not yet implemented!\n\nvertTableSize = {}".format(model['vertTableSize']))
			
			# scale verticies based on bouding box
			model['modelBoundingBox'] = {}
			vertTemp = [a['X'] for a in model['vertData']['vertex']]
			model['modelBoundingBox']['minx'] = min(vertTemp)
			model['modelBoundingBox']['maxx'] = max(vertTemp)
			vertTemp = [a['Y'] for a in model['vertData']['vertex']]
			model['modelBoundingBox']['miny'] = min(vertTemp)
			model['modelBoundingBox']['maxy'] = max(vertTemp)
			vertTemp = [a['Z'] for a in model['vertData']['vertex']]
			model['modelBoundingBox']['minz'] = min(vertTemp)
			model['modelBoundingBox']['maxz'] = max(vertTemp)
			
			if model['boundingBox'] != {"maxz": 0.0,"maxx": 0.0,"maxy": 0.0,"minx": 0.0,"miny": 0.0,"minz": 0.0}:
				for coord in 'xyz':
					for index in model['vertData']['vertex']:
						modelMin = model['modelBoundingBox']['min'+coord]
						modelMax = model['modelBoundingBox']['max'+coord]
						worldMin = model['boundingBox']['min'+coord]
						worldMax = model['boundingBox']['max'+coord]
						index[coord.upper()] = ((index[coord.upper()] - modelMin) / (modelMax - modelMin)) * (worldMax-worldMin) + worldMin
			else:
				for index in model['vertData']['vertex']:
					for coord in 'xyz':
						index[coord.upper()] /= 200.0
			
			
			fOutWrite(fOut, 'Face table\n')
			model['length3'] = readUInt32(fIn, fOut) / 6
			model['faceData'] = []
			for index in range(model['length3']):
				model['faceData'].append({})
				model['faceData'][index]['Y'] = readInt(fIn, fOut, 2)
				model['faceData'][index]['X'] = readInt(fIn, fOut, 2)
				model['faceData'][index]['Z'] = readInt(fIn, fOut, 2)
			model['facesUsed'] = model['length3']
			# cAry = new int[5];
			for index in range(5):
				# arxForm.acModel.cAry[index] = fi.read(4);
				# binaryReader.BaseStream.Position += (long) arxForm.acModel.cAry[index];
				model['cAry'] = readUInt32(fIn, fOut)
				fOutWrite(fOut, '\t')
				readStr(fIn, fOut, model['cAry'])
			# the last two iterations of the loop always seem to be 0 and I think go with the type below as an empty id
			readType(fIn, fOut)
			readStr(fIn, fOut, 3)
			fOutWrite(fOut, 'Mesh Count\n')
			model['meshCount'] = readUInt32(fIn, fOut)
			model['meshData'] = []
			model['faceCount'] = 0
			fOutWrite(fOut, 'Mesh Table\n')
			for index in range(model['meshCount']):
				readStr(fIn, fOut, 12)
				model['meshData'].append({})
				model['meshData'][index]['X'] = float(readUInt32(fIn, fOut))
				readStr(fIn, fOut, 4)
				model['meshData'][index]['materialTempID'] = float(readUInt32(fIn, fOut))
				model['meshData'][index]['vertStart'] = readUInt32(fIn, fOut) #verticy start
				model['meshData'][index]['vertCount'] = readUInt32(fIn, fOut) #number of verticies
				readStr(fIn, fOut, 4)
				model['faceCount'] += model['meshData'][index]['vertCount']
			fOutWrite(fOut, 'Shadow Count\n')
			model['shadowCount'] = readUInt32(fIn, fOut)
			model['shadowData'] = []
			fOutWrite(fOut, 'Shadow Table\n')
			for index in range(model['shadowCount']):
				readStr(fIn, fOut, 12)
				model['shadowData'].append({})
				model['shadowData'][index]['X'] = float(readUInt32(fIn, fOut))
				readStr(fIn, fOut, 4)
				model['shadowData'][index]['Y'] = float(readUInt32(fIn, fOut))
				model['shadowData'][index]['Z'] = float(readUInt32(fIn, fOut))
				model['shadowData'][index]['W'] = float(readUInt32(fIn, fOut))
				readStr(fIn, fOut, 4)
			for index in range(2):
				num4 = readUInt32(fIn, fOut)
				fOutWrite(fOut, '\t')
				readStr(fIn, fOut, num4)
		elif model['typeSwitch'] == 3:
			raise Exception('typeSwitch 3 not implimented')
			# binaryReader.BaseStream.Position += 11L;
			# arxForm.acModel.vertTableSize = (int) binaryReader.ReadByte();
			# arxForm.acModel.meshCount = fi.read(4);
			# arxForm.acModel.meshData = new arxForm.acMeshStruct[arxForm.acModel.meshCount];
			# for (int index = 0; index < arxForm.acModel.meshCount; ++index)
			# {
				# binaryReader.BaseStream.Position += 12L;
				# arxForm.acModel.meshData[index].meshTable.X = (float) fi.read(4);
				# binaryReader.BaseStream.Position += 4L;
				# arxForm.acModel.meshData[index].meshTable.Y = (float) fi.read(4);
				# arxForm.acModel.meshData[index].meshTable.Z = (float) fi.read(4);
				# arxForm.acModel.meshData[index].meshTable.W = (float) fi.read(4);
				# binaryReader.BaseStream.Position += 4L;
			# }
			# arxForm.acModel.shadowCount = fi.read(4);
			# arxForm.acModel.shadowData = new arxForm.acMeshStruct[arxForm.acModel.shadowCount];
			# for (int index = 0; index < arxForm.acModel.shadowCount; ++index)
			# {
				# binaryReader.BaseStream.Position += 12L;
				# arxForm.acModel.shadowData[index].meshTable.X = (float) fi.read(4);
				# binaryReader.BaseStream.Position += 4L;
				# arxForm.acModel.shadowData[index].meshTable.Y = (float) fi.read(4);
				# arxForm.acModel.shadowData[index].meshTable.Z = (float) fi.read(4);
				# arxForm.acModel.shadowData[index].meshTable.W = (float) fi.read(4);
				# binaryReader.BaseStream.Position += 4L;
			# }
			# int num8 = fi.read(4);
			# arxForm.acModel.vertCount = num8 / arxForm.acModel.vertTableSize;
			# arxForm.acModel.vertData = new arxForm.acVertStruct[arxForm.acModel.vertCount];
			# for (int index = 0; index < arxForm.acModel.vertCount; ++index)
			# {
			# switch (arxForm.acModel.vertTableSize)
				# {
				# case 20:
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# short num4 = fi.read(2);
					# arxForm.acModel.vertData[index].vertex.X /= (float) num4;
					# arxForm.acModel.vertData[index].vertex.Y /= (float) num4;
					# arxForm.acModel.vertData[index].vertex.Z /= (float) num4;
					# arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 2L;
					# arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
					# break;
				# case 32:
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# short num5 = fi.read(2);
					# arxForm.acModel.vertData[index].vertex.X /= (float) num5;
					# arxForm.acModel.vertData[index].vertex.Y /= (float) num5;
					# arxForm.acModel.vertData[index].vertex.Z /= (float) num5;
					# arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 6L;
					# arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();
					# break;
				# case 40:
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# short num6 = fi.read(2);
					# arxForm.acModel.vertData[index].vertex.X /= (float) num6;
					# arxForm.acModel.vertData[index].vertex.Y /= (float) num6;
					# arxForm.acModel.vertData[index].vertex.Z /= (float) num6;
					# arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 6L;
					# arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum2.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt2.W = (float) binaryReader.ReadByte();
					# break;
				# default:
					# int num7 = (int) MessageBox.Show("Not yet implemented!\n\nvertTableSize = " + (object) arxForm.acModel.vertTableSize, "Vert Read", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
					# return;
				# }
			# }
			# int num9 = fi.read(4);
			# string str3 = str1;
			# if (!(str3 == "HDMDL"))
			# {
				# if (str3 == "MDL")
				# arxForm.acModel.faceCount = num9 / 6;
			# }
			# else
				# arxForm.acModel.faceCount = num9 / 12;
			# arxForm.acModel.faceData = new arxForm.acFaceStruct[arxForm.acModel.faceCount];
			# for (int index = 0; index < arxForm.acModel.faceCount; ++index)
			# {
				# string str4 = str1;
				# if (!(str4 == "HDMDL"))
				# {
				# if (str4 == "MDL")
				# {
					# arxForm.acModel.faceData[index].faceIndex.Y = (float) binaryReader.ReadUInt16();
					# arxForm.acModel.faceData[index].faceIndex.X = (float) binaryReader.ReadUInt16();
					# arxForm.acModel.faceData[index].faceIndex.Z = (float) binaryReader.ReadUInt16();
				# }
				# }
				# else
				# {
				# arxForm.acModel.faceData[index].faceIndex.Y = (float) binaryReader.ReadUInt32();
				# arxForm.acModel.faceData[index].faceIndex.X = (float) binaryReader.ReadUInt32();
				# arxForm.acModel.faceData[index].faceIndex.Z = (float) binaryReader.ReadUInt32();
				# }
			# }
			# break;
		else:
			raise Exception("New switchType found")
		fOutWrite(fOut, 'Skin Data Table\n')
		model['length4'] = readUInt32(fIn, fOut)
		model['skinData'] = []
		for index1 in range(model['length4']):
			readStr(fIn, fOut, 17)
			model['skinData'].append({})
			model['skinData'][index1]['boneCount'] = readInt(fIn, fOut, 2)
			readStr(fIn, fOut, 11)
			model['skinData'][index1]['boneNo'] = []
			for index2 in range(model['skinData'][index1]['boneCount']):
				model['skinData'][index1]['boneNo'].append(readInt(fIn, fOut, 2))
			readStr(fIn, fOut, (256 - model['skinData'][index1]['boneCount'] * 2))
		readStr(fIn, fOut, 8)
		fOutWrite(fOut, 'Model Scale\n')
		model['modelScale'] = readFloat32(fIn, fOut)
		fOutWrite(fOut, 'Material Table\n')
		model['materialCount'] = readUInt32(fIn, fOut)
		model['materialId'] = []
		# model['materials'] = {}
		for index in range(model['materialCount']):
			# model['materials'][index] = {}
			readStr(fIn, fOut, 2)
			model['materialId'].append(readID(app, fIn, fOut))
			
			
		ReadRest(fIn, fOut)
			
		fIn.close()
		# if dev:
		# 	fOut.close()
		# 	print data["dir"]+'.format'
		# 	os.system('"'+data['dir']+'.format"')
	else:
		raise Exception("Error reading model file!")
	tmpdict = open(data['dir'].replace('.acu', '.json'), 'w')
	tmpdict.write(json.dumps(model))
	tmpdict.close()
