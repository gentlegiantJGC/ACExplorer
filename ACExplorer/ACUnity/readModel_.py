import os
import numpy
from ACExplorer.ACUnity.formatFile import readID, readStr, readUInt32, readFloat32, readType, fOutWrite, ReadRest


def read_model(app, file_id):
	"""
	Given a numerical file_id will get the file and return a Model class populated with all the data
	:param app: Class instance of ACExplorerMain.App
	:param file_id: Int
	:return: Class Model
	"""

	data = app.tempNewFiles.getData(file_id)
	if data is None:
		app.log.warn(__name__, 'Failed to find file {:016X}'.format(file_id))
		return
	model_file = app.misc.FileObject()
	model_file.write(data['rawFile'])
	model_file.seek(0)
	
	if app.dev:
		formatted_file = app.misc.FileObject(
			'{}.format'.format(
				os.path.join(
					app.CONFIG['dumpFolder'],
					app.gameFunctions.gameIdentifier,
					data['forgeFile'],
					'{:016X}'.format(data['datafileID']),
					data['fileType'],
					data['fileName']
				)
			)
		, 'w')
	else:
		formatted_file = None

	model = app.misc.mesh.Model()
	model.name = data['fileName']
	
	readStr(model_file, formatted_file, 2)
	readID(app, model_file, formatted_file)
	file_type = readType(model_file, formatted_file)
	if file_type != '415D9568':
		return
	fOutWrite(formatted_file, '\n')
	readStr(model_file, formatted_file, 1)		#skip an empty byte
	model.type = readStr(model_file, formatted_file, 4)	#
	readStr(model_file, formatted_file, 1)
	a_count = readUInt32(model_file, formatted_file)
	if a_count > 0:
		raise Exception('aCount not accounted for')
	# {
		# readStr(model_file, formatted_file, 1)
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
	bone_count = readUInt32(model_file, formatted_file)
	if bone_count > 0:
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
	
	# readStr(model_file, formatted_file, 41)
	model.bounding_box = numpy.fromstring(model_file.read(32), numpy.float32).reshape(2, 4)
	fOutWrite(formatted_file, '{}\n'.format(model.bounding_box))

	readStr(model_file, formatted_file, 1)

	readID(app, model_file, formatted_file)
	if readType(model_file, formatted_file) == "FC9E1595":
		readStr(model_file, formatted_file, 4)
		fOutWrite(formatted_file, 'Typeswitch\n')
		model.type_switch = readStr(model_file, formatted_file, 1)
		if model.type_switch == '00':
			readID(app, model_file, formatted_file)
			readType(model_file, formatted_file)
			readStr(model_file, formatted_file, 5)
			fOutWrite(formatted_file, 'Vert table width\n')
			vert_table_width = readUInt32(model_file, formatted_file)
			readUInt32(model_file, formatted_file)
			bounding_box2 = numpy.fromstring(model_file.read(24), numpy.float32).reshape(2, 3)
			fOutWrite(formatted_file, '{}\n'.format(bounding_box2))
			mesh_face_block_count = readUInt32(model_file, formatted_file)
			shadow_face_block_count = readUInt32(model_file, formatted_file)
			fOutWrite(formatted_file, 'Mesh Face Blocks\n')
			mesh_face_blocks = numpy.fromstring(model_file.read(4*mesh_face_block_count), numpy.uint32)
			fOutWrite(formatted_file, '{}\n'.format(mesh_face_blocks))
			shadow_face_blocks = numpy.fromstring(model_file.read(4*shadow_face_block_count), numpy.uint32)
			fOutWrite(formatted_file, '{}\n'.format(shadow_face_blocks))
			readUInt32(model_file, formatted_file)
			readStr(model_file, formatted_file, 1)
			fOutWrite(formatted_file, '\nVert table\n')
			vert_table_length = readUInt32(model_file, formatted_file)
			model.vert_count = vert_table_length / vert_table_width

			vert_table = model_file.read(vert_table_length)

			if vert_table_width == 16:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('', numpy.int16, 2),  # not sure what this is
					('vt', numpy.int16, 2)
				])

			elif vert_table_width == 20:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('n', numpy.int16, 3),
					('', numpy.int16),  # not sure what this is
					('vt', numpy.int16, 2)
				])

			elif vert_table_width == 24:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('n', numpy.int16, 3),
					('', numpy.int16, 3),  # not sure what this is
					('vt', numpy.int16, 2)
				])

			elif vert_table_width == 28:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('n', numpy.int16, 3),
					('', numpy.int16, 3),  # not sure what this is
					('vt', numpy.int16, 2),
					('', numpy.int16, 2),  # not sure what this is
				])

			elif vert_table_width == 32:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('n', numpy.int16, 3),
					('', numpy.int16, 3),  # not sure what this is
					('vt', numpy.int16, 2),
					('bn', numpy.uint8, 4),
					('bw', numpy.uint8, 4)
				])

			elif vert_table_width == 36:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('n', numpy.int16, 3),
					('', numpy.int16, 3),  # not sure what this is
					('vt', numpy.int16, 2),
					('', numpy.int16, 2),  # not sure what this is
					('bn', numpy.uint8, 4),
					('bw', numpy.uint8, 4)
				])

			elif vert_table_width == 40:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('n', numpy.int16, 3),
					('', numpy.int16, 3),  # not sure what this is
					('vt', numpy.int16, 2),
					('bn', numpy.uint8, 4),
					('bn2', numpy.uint8, 4),
					('bw', numpy.uint8, 4),
					('bw2', numpy.uint8, 4)
				])

			elif vert_table_width == 48:
				vert_table = numpy.fromstring(vert_table, dtype=[
					('v', numpy.int16, 3),
					('sc', numpy.int16),
					('n', numpy.int16, 3),
					('', numpy.int16, 3),  # not sure what this is
					('vt', numpy.int16, 2),
					('', numpy.int16, 2),  # not sure what this is
					('bn', numpy.uint8, 4),
					('bn2', numpy.uint8, 4),
					('bw', numpy.uint8, 4),
					('bw2', numpy.uint8, 4),
					('', numpy.int16, 2),  # not sure what this is
				])
			else:
				app.log.warn(__name__, 'Not yet implemented!\n\nvertTableWidth = {}'.format(vert_table_width))
				return

			fOutWrite(formatted_file, '{}\n'.format(vert_table))

			model.vertices = vert_table['v'].astype(numpy.float) / vert_table['sc'].reshape(-1, 1).astype(numpy.float)
			model.texture_vertices = vert_table['vt'].astype(numpy.float) / 2048.0
			model.texture_vertices[:, 1] *= -1
			model.normals = vert_table['n'].astype(numpy.float)
			
			# # scale verticies based on bouding box
			# model['modelBoundingBox'] = {}
			# vertTemp = [a['X'] for a in model['vertData']['vertex']]
			# model['modelBoundingBox']['minx'] = min(vertTemp)
			# model['modelBoundingBox']['maxx'] = max(vertTemp)
			# vertTemp = [a['Y'] for a in model['vertData']['vertex']]
			# model['modelBoundingBox']['miny'] = min(vertTemp)
			# model['modelBoundingBox']['maxy'] = max(vertTemp)
			# vertTemp = [a['Z'] for a in model['vertData']['vertex']]
			# model['modelBoundingBox']['minz'] = min(vertTemp)
			# model['modelBoundingBox']['maxz'] = max(vertTemp)
			#
			# if model['boundingBox'] != {"maxz": 0.0,"maxx": 0.0,"maxy": 0.0,"minx": 0.0,"miny": 0.0,"minz": 0.0}:
			# 	for coord in 'xyz':
			# 		for index in model['vertData']['vertex']:
			# 			modelMin = model['modelBoundingBox']['min'+coord]
			# 			modelMax = model['modelBoundingBox']['max'+coord]
			# 			worldMin = model['boundingBox']['min'+coord]
			# 			worldMax = model['boundingBox']['max'+coord]
			# 			index[coord.upper()] = ((index[coord.upper()] - modelMin) / (modelMax - modelMin)) * (worldMax-worldMin) + worldMin
			# else:
			# 	for index in model['vertData']['vertex']:
			# 		for coord in 'xyz':
			# 			index[coord.upper()] /= 200.0
			
			fOutWrite(formatted_file, 'Face table\n')
			face_table_length = readUInt32(model_file, formatted_file)
			face_table = numpy.fromstring(model_file.read(face_table_length), numpy.uint16).reshape(-1, 3) + 1
			fOutWrite(formatted_file, '{}\n'.format(face_table))
			model.faces = numpy.split(face_table, numpy.cumsum(mesh_face_blocks * 64)[:-1])
			#
			#
			# mesh_face_blocks_x64 = numpy.cumsum(mesh_face_blocks * 64)
			# mesh_face_blocks_x64[-1] =
			# mesh_face_blocks[-1] =* 64 * 6 == face_table_length:
			# 	model.faces = [face_table[64*mesh_face_blocks[index-1]:64*block_count] for index, block_count in enumerate(mesh_face_blocks)]
			# model.faces = [face_table[:64 * block_count] if index==0 else face_table[64*mesh_face_blocks[index-1]:64*block_count] for index, block_count in enumerate(mesh_face_blocks)]

			for _ in range(3):
				readStr(model_file, formatted_file, readUInt32(model_file, formatted_file), 1)

			readID(app, model_file, formatted_file)
			readType(model_file, formatted_file)
			readStr(model_file, formatted_file, 3)
			fOutWrite(formatted_file, 'Mesh Table\n')
			mesh_count = readUInt32(model_file, formatted_file)
			model.meshes = numpy.fromstring(model_file.read(36 * mesh_count), dtype=[
				('file_id', numpy.uint64),
				('file_type', numpy.uint32),
				('verts_used', numpy.uint32),
				('', numpy.uint32),
				('vert_count', numpy.uint32),
				('faces_used_x3', numpy.uint32),
				('face_count', numpy.uint32),
				('', numpy.uint32)
			])
			fOutWrite(formatted_file, '{}\n'.format(model.meshes))

			for index, verts_used in enumerate(model.meshes['verts_used']):
				model.faces[index] += verts_used

			fOutWrite(formatted_file, 'Shadow Table\n')
			shadow_count = readUInt32(model_file, formatted_file)
			shadow_table = numpy.fromstring(model_file.read(36 * shadow_count), dtype=[
				('file_id', numpy.uint64),
				('file_type', numpy.uint32),
				('X', numpy.uint32),
				('', numpy.uint32),
				('Y', numpy.uint32),
				('Z', numpy.uint32),
				('W', numpy.uint32),
				('', numpy.uint32),
			])
			fOutWrite(formatted_file, '{}\n'.format(shadow_table))

			for index in range(2):
				readStr(model_file, formatted_file, readUInt32(model_file, formatted_file), 1)

		elif model.type_switch == '03':
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

		fOutWrite(formatted_file, 'Skin Data Table\n')
		skin_count = readUInt32(model_file, formatted_file)
		skin_table = numpy.fromstring(model_file.read(286 * skin_count), dtype=[
			('file_id', numpy.uint64),
			('file_type', numpy.uint32),
			('', numpy.int8),
			('', numpy.uint32),
			('bone_count', numpy.uint16),
			('', numpy.int8, 11),
			('bones', numpy.uint16, 128)
		])
		fOutWrite(formatted_file, '{}\n'.format(skin_table))

		readStr(model_file, formatted_file, 8)
		fOutWrite(formatted_file, 'Model Scale?\n')
		model_scale = readFloat32(model_file, formatted_file)
		fOutWrite(formatted_file, 'Material Table\n')
		material_count = readUInt32(model_file, formatted_file)
		material_table = numpy.fromstring(model_file.read(10 * material_count), dtype=[
			('', numpy.uint16),
			('file_id', numpy.uint64)
		])
		fOutWrite(formatted_file, '{}\n'.format(material_table))
		model.materials = material_table['file_id']

		ReadRest(model_file, formatted_file)

	else:
		raise Exception("Error reading model file!")

	if app.dev:
		formatted_file.save()
		os.startfile(formatted_file.path)
	return model
