from ACExplorer.ACUnity.decompressDatafile import decompressDatafile
from ACExplorer.misc import tempFiles
from ACExplorer.misc.dataTypes import BEHEX2, LE2BE2, LE2DEC2, float32
import json


def readModel(fileTree, fileList, fileID):
	if not tempFiles.exists(fileID):
		decompressDatafile(fileTree, fileList, fileID)
	data = tempFiles.read(fileID)
	if len(data) == 0:
		raise Exception('file '+fileID+' is empty')
	data = data[0]
	# str1 = strArray[1]			#MDL or HDMDL
	fi = open(data['dir'], 'rb')				#open parent file
	_ = fi.read(10);										# jump to after header
	# fileID = BEHEX2(fi.read(8))		#file id
	model = {}
	# model['workingDir'] = workingDir
	model['fileType'] = LE2BE2(fi.read(4))	#file type
	_ = fi.read(1)		#skip and empty byte
	model['modelType'] = LE2BE2(fi.read(4))	#
	_ = fi.read(1)
	model['aCount'] = LE2DEC2(fi.read(4))
	if model['aCount'] > 0:
		raise Exception('aCount not accounted for')
	# {
		# _ = fi.read(1)
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
	model['boneCount'] = LE2DEC2(fi.read(4))
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
	_ = fi.read(41)
	if LE2BE2(fi.read(4)).upper() == "FC9E1595":
		_ = fi.read(4)
		model['typeSwitch'] = LE2DEC2(fi.read(4))
		if model['typeSwitch'] == 0:
			_ = fi.read(14)
			model['vertTableSize'] = LE2DEC2(fi.read(4))
			model['unkLng2'] = LE2DEC2(fi.read(4))
			_ = fi.read(24)
			model['length1'] = LE2DEC2(fi.read(4))
			model['length2'] = LE2DEC2(fi.read(4))
			model['meshFaceBlocks'] = []
			model['shadowFaceBlocks'] = []
			for index in range(model['length1']):
				model['meshFaceBlocks'].append(LE2DEC2(fi.read(4)))
			for index in range(model['length2']):
				model['shadowFaceBlocks'].append(LE2DEC2(fi.read(4)))
			model['unkLng'] = LE2DEC2(fi.read(4))
			model['unkByt'] = fi.read(1);
			num3 = LE2DEC2(fi.read(4))
			model['vertCount'] = num3 / model['vertTableSize'];
			model['vertData'] = {}
			model['vertData']['vertex'] = []
			model['vertData']['tVert'] = []
			model['vertData']['normals'] = []
			# arxForm.acModel.vertData = new arxForm.acVertStruct[arxForm.acModel.vertCount];
			for index in range(model['vertCount']):
				if model['vertTableSize'] == 40:
					raise Exception('40')
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 2L;
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
				elif model['vertTableSize'] == 48:
					raise Exception('48')
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 2L;
					# arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 6L;
					# arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 4L;
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
					# binaryReader.BaseStream.Position += 4L;
					# break;
				elif model['vertTableSize'] == 32:
					raise Exception('32')
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 2L;
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
				elif model['vertTableSize'] == 36:
					raise Exception('36')
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 2L;
					# arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 6L;
					# arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 4L;
					# arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
					# arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();
					# break;
				elif model['vertTableSize'] == 24:
					raise Exception('24')
					# arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 2L;
					# arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
					# arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
					# binaryReader.BaseStream.Position += 6L;
					# arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
					# arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
					# break;
				elif model['vertTableSize'] == 28:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['X'] >= 2**15:
						model['vertData']['vertex'][index]['X'] -= 2**16
					model['vertData']['vertex'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['Y'] >= 2**15:
						model['vertData']['vertex'][index]['Y'] -= 2**16
					model['vertData']['vertex'][index]['Z'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['Z'] >= 2**15:
						model['vertData']['vertex'][index]['Z'] -= 2**16
					num4 = float(LE2DEC2(fi.read(2)))
					if num4 >= 2**15:
						num4 -= 2**16
					model['vertData']['vertex'][index]['X'] /= num4
					model['vertData']['vertex'][index]['Y'] /= num4
					model['vertData']['vertex'][index]['Z'] /= num4
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['normals'][index]['X'] >= 2**15:
						model['vertData']['normals'][index]['X'] -= 2**16
					model['vertData']['normals'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['normals'][index]['Y'] >= 2**15:
						model['vertData']['normals'][index]['Y'] -= 2**16
					model['vertData']['normals'][index]['Z'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['normals'][index]['Z'] >= 2**15:
						model['vertData']['normals'][index]['Z'] -= 2**16
					_ = fi.read(6)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['tVert'][index]['X'] >= 2**15:
						model['vertData']['tVert'][index]['X'] -= 2**16
					model['vertData']['tVert'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['tVert'][index]['Y'] >= 2**15:
						model['vertData']['tVert'][index]['Y'] -= 2**16
					_ = fi.read(4)
				elif model['vertTableSize'] == 16:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['X'] >= 2**15:
						model['vertData']['vertex'][index]['X'] -= 2**16
					model['vertData']['vertex'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['Y'] >= 2**15:
						model['vertData']['vertex'][index]['Y'] -= 2**16
					model['vertData']['vertex'][index]['Z'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['Z'] >= 2**15:
						model['vertData']['vertex'][index]['Z'] -= 2**16
					num5 = float(LE2DEC2(fi.read(2)))
					if num5 >= 2**15:
						num5 -= 2**16
					model['vertData']['vertex'][index]['X'] /= num5
					model['vertData']['vertex'][index]['Y'] /= num5
					model['vertData']['vertex'][index]['Z'] /= num5
					_ = fi.read(4)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['tVert'][index]['X'] >= 2**15:
						model['vertData']['tVert'][index]['X'] -= 2**16
					model['vertData']['tVert'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['tVert'][index]['Y'] >= 2**15:
						model['vertData']['tVert'][index]['Y'] -= 2**16
				elif model['vertTableSize'] == 20:
					model['vertData']['vertex'].append({})
					model['vertData']['vertex'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['X'] >= 2**15:
						model['vertData']['vertex'][index]['X'] -= 2**16
					model['vertData']['vertex'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['Y'] >= 2**15:
						model['vertData']['vertex'][index]['Y'] -= 2**16
					model['vertData']['vertex'][index]['Z'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['vertex'][index]['Z'] >= 2**15:
						model['vertData']['vertex'][index]['Z'] -= 2**16
					num6 = float(LE2DEC2(fi.read(2)))
					if num6 >= 2**15:
						num6 -= 2**16
					model['vertData']['vertex'][index]['X'] /= num6
					model['vertData']['vertex'][index]['Y'] /= num6
					model['vertData']['vertex'][index]['Z'] /= num6
					model['vertData']['normals'].append({})
					model['vertData']['normals'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['normals'][index]['X'] >= 2**15:
						model['vertData']['normals'][index]['X'] -= 2**16
					model['vertData']['normals'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['normals'][index]['Y'] >= 2**15:
						model['vertData']['normals'][index]['Y'] -= 2**16
					model['vertData']['normals'][index]['Z'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['normals'][index]['Z'] >= 2**15:
						model['vertData']['normals'][index]['Z'] -= 2**16
					_ = fi.read(2)
					model['vertData']['tVert'].append({})
					model['vertData']['tVert'][index]['X'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['tVert'][index]['X'] >= 2**15:
						model['vertData']['tVert'][index]['X'] -= 2**16
					model['vertData']['tVert'][index]['Y'] = float(LE2DEC2(fi.read(2)))
					if model['vertData']['tVert'][index]['Y'] >= 2**15:
						model['vertData']['tVert'][index]['Y'] -= 2**16
				else:
					raise Exception("Not yet implemented!\n\nvertTableSize = " + str(vertTableSize))
			model['length3'] = LE2DEC2(fi.read(4)) / 6
			model['faceData'] = []
			for index in range(model['length3']):
				model['faceData'].append({})
				model['faceData'][index]['Y'] = LE2DEC2(fi.read(2))
				model['faceData'][index]['X'] = LE2DEC2(fi.read(2))
				model['faceData'][index]['Z'] = LE2DEC2(fi.read(2))
			model['facesUsed'] = model['length3'];
			# cAry = new int[5];
			for index in range(5):
				# arxForm.acModel.cAry[index] = fi.read(4);
				# binaryReader.BaseStream.Position += (long) arxForm.acModel.cAry[index];
				model['cAry'] = LE2DEC2(fi.read(4))
				_ = fi.read(model['cAry'])
			_ = fi.read(7)
			model['meshCount'] = LE2DEC2(fi.read(4))
			model['meshData'] = []
			model['faceCount'] = 0
			for index in range(model['meshCount']):
				_ = fi.read(12)
				model['meshData'].append({})
				model['meshData'][index]['X'] = float(LE2DEC2(fi.read(4)))
				_ = fi.read(4)
				model['meshData'][index]['materialTempID'] = float(LE2DEC2(fi.read(4)))
				model['meshData'][index]['vertStart'] = LE2DEC2(fi.read(4)) #verticy start
				model['meshData'][index]['vertCount'] = LE2DEC2(fi.read(4)) #number of verticies
				_ = fi.read(4)
				model['faceCount'] += model['meshData'][index]['vertCount']
			model['shadowCount'] = LE2DEC2(fi.read(4))
			model['shadowData'] = []
			for index in range(model['shadowCount']):
				_ = fi.read(12)
				model['shadowData'].append({})
				model['shadowData'][index]['X'] = float(LE2DEC2(fi.read(4)))
				_ = fi.read(4)
				model['shadowData'][index]['Y'] = float(LE2DEC2(fi.read(4)))
				model['shadowData'][index]['Z'] = float(LE2DEC2(fi.read(4)))
				model['shadowData'][index]['W'] = float(LE2DEC2(fi.read(4)))
				_ = fi.read(4)
			for index in range(2):
				num4 = LE2DEC2(fi.read(4))
				_ = fi.read(num4)
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
		model['length4'] = LE2DEC2(fi.read(4))
		model['skinData'] = []
		for index1 in range(model['length4']):
			_ = fi.read(17)
			model['skinData'].append({})
			model['skinData'][index1]['boneCount'] = LE2DEC2(fi.read(2))
			_ = fi.read(11)
			model['skinData'][index1]['boneNo'] = []
			for index2 in range(model['skinData'][index1]['boneCount']):
				model['skinData'][index1]['boneNo'].append(LE2DEC2(fi.read(2)))
			_ = fi.read((256 - model['skinData'][index1]['boneCount'] * 2))
		_ = fi.read(8)
		model['modelScale'] = float32(fi.read(4))
		model['materialCount'] = LE2DEC2(fi.read(4))
		model['materialId'] = []
		# model['materials'] = {}
		for index in range(model['materialCount']):
			# model['materials'][index] = {}
			_ = fi.read(2)
			model['materialId'].append(BEHEX2(fi.read(8)).upper())
		fi.close()
	else:
		raise Exception("Error reading model file!")
	tmpdict = open(data['dir'].replace('.acu', '.json'), 'w')
	tmpdict.write(json.dumps(model))
	tmpdict.close()
