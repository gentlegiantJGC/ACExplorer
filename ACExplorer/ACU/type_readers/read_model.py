from ACExplorer.misc.mesh import BaseModel
import numpy

file_type = '415D9568'


def plugin(app, file_object_data_wrapper, out_file, indent_count):
	return Model(app, file_object_data_wrapper, out_file, indent_count)


class Model(BaseModel):
	def __init__(self, app, model_file, out_file, indent_count):
		BaseModel.__init__(self)

		model_file.out_file_write('\n', out_file, indent_count)
		model_file.read_str(1, out_file, indent_count)  # skip an empty byte
		self.type = model_file.read_str(4, out_file, indent_count)
		model_file.read_str(1, out_file, indent_count)
		a_count = model_file.read_uint_32(out_file, indent_count)
		if a_count > 0:
			raise Exception('aCount not accounted for')
		# {
		# 	model_file.read_str(1, out_file, indent_count)
		# 	for (int index1 = 0; index1 < 2; ++index1)
		# 	{
		# 		  binaryReader.BaseStream.Position += 13L;
		# 		  if (fi.read(4) > 0)
		# 		  {
		# 			int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 1 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
		# 			return;
		# 		  }
		# 		  int num4 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num4 * 4);
		# 		  int num5 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num5 * 4);
		# 		  int num6 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num6 * 4);
		# 		  int num7 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) num7;
		# 		  int num8 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num8 * 12);
		# 		  int num9 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num9 * 12);
		# 		  int num10 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num10 * 12);
		# 		  int num11 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num11 * 12);
		# 		  int num12 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num12 * 4);
		# 		  if (fi.read(4) > 0)
		# 		  {
		# 			int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 11 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
		# 			return;
		# 		  }
		# 		  ++binaryReader.BaseStream.Position;
		# 		  int num13 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num13 * 4);
		# 		  int num14 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num14 * 2);
		# 		  int num15 = fi.read(4);
		# 		  binaryReader.BaseStream.Position += (long) (num15 * 2);
		# 		  int num16 = fi.read(4);
		# 		  for (int index2 = 0; index2 < num16; ++index2)
		# 		  {
		# 			if (fi.read(4) > 0)
		# 			{
		# 			  int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 15 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
		# 			  return;
		# 			}
		# 			if (fi.read(4) > 0)
		# 			{
		# 			  int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 16 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
		# 			  return;
		# 			}
		# 			binaryReader.BaseStream.Position += 4L;
		# 			if (fi.read(4) > 0)
		# 			{
		# 			  int num3 = (int) MessageBox.Show("Undetermined block of model information.", "Block 17 Issue", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
		# 			  return;
		# 			}
		# 			++binaryReader.BaseStream.Position;
		# 			int num17 = fi.read(4);
		# 			binaryReader.BaseStream.Position += (long) (num17 * 8);
		# 			int num18 = fi.read(4);
		# 			binaryReader.BaseStream.Position += (long) (num18 * 4);
		# 		}
		# 		binaryReader.BaseStream.Position += 12L;
		# 	}
		# }
		bone_count = model_file.read_uint_32(out_file, indent_count)
		if bone_count > 0:
			raise Exception('boneCount not accounted for')
		# {
		# arxForm.acModel.boneStruct = new arxForm.acBoneStruct[arxForm.acModel.boneCount];
		# for (int index = 0; index < arxForm.acModel.boneCount; ++index)
		# {
		#   arxForm.acModel.boneStruct[index].boneID = string.Format("{0:X8}", (object) fi.read(8)).PadLeft(16, '0');
		#   arxForm.acModel.boneStruct[index].boneType = string.Format("{0:X4}", (object) fi.read(4)).PadLeft(8, '0');
		#   arxForm.acModel.boneStruct[index].boneName = string.Format("{0:X4}", (object) fi.read(4)).PadLeft(8, '0');
		#   arxForm.acModel.boneStruct[index].transMatrix.M11 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M12 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M13 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M14 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M21 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M22 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M23 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M24 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M31 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M32 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M33 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M34 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M41 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M42 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M43 = binaryReader.ReadSingle();
		#   arxForm.acModel.boneStruct[index].transMatrix.M44 = binaryReader.ReadSingle();
		#   ++binaryReader.BaseStream.Position;
		#   arxForm.acModel.boneStruct[index].transMatrix.Invert();
		# }
		# }

		# readStr(model_file, out_file, 41)
		self.bounding_box = model_file.read_numpy(numpy.float32, 32, out_file, indent_count).reshape(2, 4)
		model_file.out_file_write(f'{self.bounding_box}\n', out_file, indent_count)

		model_file.read_str(1, out_file, indent_count)

		model_file.read_id(out_file, indent_count)
		if model_file.read_type(out_file, indent_count) == "FC9E1595":  # this part should get moved to a different file technically
			model_file.read_str(4, out_file, indent_count)
			model_file.out_file_write('Typeswitch\n', out_file, indent_count)
			self.type_switch = model_file.read_str(1, out_file, indent_count)
			if self.type_switch == b'\x00':
				model_file.read_id(out_file, indent_count)
				model_file.read_type(out_file, indent_count)
				model_file.read_str(5, out_file, indent_count)
				model_file.out_file_write('Vert table width\n', out_file, indent_count)
				vert_table_width = model_file.read_uint_32(out_file, indent_count)
				model_file.read_uint_32(out_file, indent_count)
				bounding_box2 = model_file.read_numpy(numpy.float32, 24, out_file, indent_count).reshape(2, 3)
				model_file.out_file_write(f'{bounding_box2}\n', out_file, indent_count)
				mesh_face_block_count = model_file.read_uint_32(out_file, indent_count)
				shadow_face_block_count = model_file.read_uint_32(out_file, indent_count)
				model_file.out_file_write('Mesh Face Blocks\n', out_file, indent_count)
				mesh_face_blocks = model_file.read_numpy(numpy.uint32, 4*mesh_face_block_count, out_file, indent_count)
				model_file.out_file_write(f'{mesh_face_blocks}\n', out_file, indent_count)
				shadow_face_blocks = model_file.read_numpy(numpy.uint32, 4*shadow_face_block_count, out_file, indent_count)
				model_file.out_file_write(f'{shadow_face_blocks}\n', out_file, indent_count)
				model_file.read_uint_32(out_file, indent_count)
				model_file.read_str(1, out_file, indent_count)
				model_file.out_file_write('\nVert table\n', out_file, indent_count)
				vert_table_length = model_file.read_uint_32(out_file, indent_count)
				self.vert_count = vert_table_length / vert_table_width

				if vert_table_width == 16:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('', numpy.int16, 2),  # not sure what this is
						('vt', numpy.int16, 2)
					], vert_table_length, out_file, indent_count)

				elif vert_table_width == 20:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16),  # not sure what this is
						('vt', numpy.int16, 2)
					], vert_table_length, out_file, indent_count)

				elif vert_table_width == 24:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2)
					], vert_table_length, out_file, indent_count)

				elif vert_table_width == 28:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('', numpy.int16, 2),  # not sure what this is
					], vert_table_length, out_file, indent_count)

				elif vert_table_width == 32:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('bn', numpy.uint8, 4),
						('bw', numpy.uint8, 4)
					], vert_table_length, out_file, indent_count)

				elif vert_table_width == 36:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('', numpy.int16, 2),  # not sure what this is
						('bn', numpy.uint8, 4),
						('bw', numpy.uint8, 4)
					], vert_table_length, out_file, indent_count)

				elif vert_table_width == 40:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('bn', numpy.uint8, 4),
						('bn2', numpy.uint8, 4),
						('bw', numpy.uint8, 4),
						('bw2', numpy.uint8, 4)
					], vert_table_length, out_file, indent_count)

				elif vert_table_width == 48:
					vert_table = model_file.read_numpy([
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
					], vert_table_length, out_file, indent_count)
				else:
					app.log.warn(__name__, 'Not yet implemented!\n\nvertTableWidth = {}'.format(vert_table_width))
					return

				model_file.out_file_write(f'{vert_table}\n', out_file, indent_count)

				self.vertices = vert_table['v'].astype(numpy.float) / vert_table['sc'].reshape(-1, 1).astype(numpy.float)
				self.vertices *= numpy.sum(bounding_box2, 0) / numpy.amax(self.vertices, 0)
				# for dim in range(3):
				# 	self.vertices[:, dim] = numpy.interp(self.vertices[:, dim], (self.vertices[:, dim].min(), self.vertices[:, dim].max()), bounding_box2[:, dim])
				self.texture_vertices = vert_table['vt'].astype(numpy.float) / 2048.0
				self.texture_vertices[:, 1] *= -1
				if 'n' in vert_table:
					self.normals = vert_table['n'].astype(numpy.float)

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

				model_file.out_file_write('Face table\n', out_file, indent_count)
				face_table_length = model_file.read_uint_32(out_file, indent_count)
				face_table = model_file.read_numpy(numpy.uint16, face_table_length, out_file, indent_count).reshape(-1, 3) + 1
				model_file.out_file_write(f'{face_table}\n', out_file, indent_count)
				self.faces = numpy.split(face_table, numpy.cumsum(mesh_face_blocks * 64)[:-1])
				#
				#
				# mesh_face_blocks_x64 = numpy.cumsum(mesh_face_blocks * 64)
				# mesh_face_blocks_x64[-1] =
				# mesh_face_blocks[-1] =* 64 * 6 == face_table_length:
				# 	self.faces = [face_table[64*mesh_face_blocks[index-1]:64*block_count] for index, block_count in enumerate(mesh_face_blocks)]
				# self.faces = [face_table[:64 * block_count] if index==0 else face_table[64*mesh_face_blocks[index-1]:64*block_count] for index, block_count in enumerate(mesh_face_blocks)]

				for _ in range(3):
					count = model_file.read_uint_32(out_file, indent_count)
					model_file.read_str(count, out_file, indent_count)

				model_file.read_id(out_file, indent_count)
				model_file.read_type(out_file, indent_count)
				model_file.read_str(3, out_file, indent_count)
				model_file.out_file_write('Mesh Table\n', out_file, indent_count)
				mesh_count = model_file.read_uint_32(out_file, indent_count)
				self.meshes = model_file.read_numpy([
					('file_id', numpy.uint64),
					('file_type', numpy.uint32),
					('verts_used', numpy.uint32),
					('', numpy.uint32),
					('vert_count', numpy.uint32),
					('faces_used_x3', numpy.uint32),
					('face_count', numpy.uint32),
					('', numpy.uint32)
				], 36 * mesh_count, out_file, indent_count)

				model_file.out_file_write(f'{self.meshes}\n', out_file, indent_count)

				for index, verts_used in enumerate(self.meshes['verts_used']):
					self.faces[index] += verts_used

				model_file.out_file_write('Shadow Table\n', out_file, indent_count)
				shadow_count = model_file.read_uint_32(out_file, indent_count)
				shadow_table = model_file.read_numpy([
					('file_id', numpy.uint64),
					('file_type', numpy.uint32),
					('X', numpy.uint32),
					('', numpy.uint32),
					('Y', numpy.uint32),
					('Z', numpy.uint32),
					('W', numpy.uint32),
					('', numpy.uint32),
				], 36 * shadow_count, out_file, indent_count)

				model_file.out_file_write(f'{shadow_table}\n', out_file, indent_count)

				for index in range(2):
					count = model_file.read_uint_32(out_file, indent_count)
					model_file.read_str(count, out_file, indent_count+1)

			elif self.type_switch == b'\x03':
				raise Exception('typeSwitch 3 not implimented')
				# binaryReader.BaseStream.Position += 11L;
				# arxForm.acModel.vertTableSize = (int) binaryReader.ReadByte();
				# arxForm.acModel.meshCount = fi.read(4);
				# arxForm.acModel.meshData = new arxForm.acMeshStruct[arxForm.acModel.meshCount];
				# for (int index = 0; index < arxForm.acModel.meshCount; ++index)
				# {
				# 	binaryReader.BaseStream.Position += 12L;
				# 	arxForm.acModel.meshData[index].meshTable.X = (float) fi.read(4);
				# 	binaryReader.BaseStream.Position += 4L;
				# 	arxForm.acModel.meshData[index].meshTable.Y = (float) fi.read(4);
				# 	arxForm.acModel.meshData[index].meshTable.Z = (float) fi.read(4);
				# 	arxForm.acModel.meshData[index].meshTable.W = (float) fi.read(4);
				# 	binaryReader.BaseStream.Position += 4L;
				# }
				# arxForm.acModel.shadowCount = fi.read(4);
				# arxForm.acModel.shadowData = new arxForm.acMeshStruct[arxForm.acModel.shadowCount];
				# for (int index = 0; index < arxForm.acModel.shadowCount; ++index)
				# {
				# 	binaryReader.BaseStream.Position += 12L;
				# 	arxForm.acModel.shadowData[index].meshTable.X = (float) fi.read(4);
				# 	binaryReader.BaseStream.Position += 4L;
				# 	arxForm.acModel.shadowData[index].meshTable.Y = (float) fi.read(4);
				# 	arxForm.acModel.shadowData[index].meshTable.Z = (float) fi.read(4);
				# 	arxForm.acModel.shadowData[index].meshTable.W = (float) fi.read(4);
				# 	binaryReader.BaseStream.Position += 4L;
				# }
				# int num8 = fi.read(4);
				# arxForm.acModel.vertCount = num8 / arxForm.acModel.vertTableSize;
				# arxForm.acModel.vertData = new arxForm.acVertStruct[arxForm.acModel.vertCount];
				# for (int index = 0; index < arxForm.acModel.vertCount; ++index)
				# {
				# switch (arxForm.acModel.vertTableSize)
				# 	{
				# 	case 20:
				# 		arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
				# 		short num4 = fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.X /= (float) num4;
				# 		arxForm.acModel.vertData[index].vertex.Y /= (float) num4;
				# 		arxForm.acModel.vertData[index].vertex.Z /= (float) num4;
				# 		arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
				# 		binaryReader.BaseStream.Position += 2L;
				# 		arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
				# 		break;
				# 	case 32:
				# 		arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
				# 		short num5 = fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.X /= (float) num5;
				# 		arxForm.acModel.vertData[index].vertex.Y /= (float) num5;
				# 		arxForm.acModel.vertData[index].vertex.Z /= (float) num5;
				# 		arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
				# 		binaryReader.BaseStream.Position += 6L;
				# 		arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();
				# 		break;
				# 	case 40:
				# 		arxForm.acModel.vertData[index].vertex.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.Z = (float) fi.read(2);
				# 		short num6 = fi.read(2);
				# 		arxForm.acModel.vertData[index].vertex.X /= (float) num6;
				# 		arxForm.acModel.vertData[index].vertex.Y /= (float) num6;
				# 		arxForm.acModel.vertData[index].vertex.Z /= (float) num6;
				# 		arxForm.acModel.vertData[index].normals.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].normals.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].normals.Z = (float) fi.read(2);
				# 		binaryReader.BaseStream.Position += 6L;
				# 		arxForm.acModel.vertData[index].tVert.X = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].tVert.Y = (float) fi.read(2);
				# 		arxForm.acModel.vertData[index].boneNum.X = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum.Y = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum.Z = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum.W = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum2.X = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum2.Y = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum2.Z = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneNum2.W = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.X = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.Y = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.Z = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt.W = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt2.X = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt2.Y = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt2.Z = (float) binaryReader.ReadByte();
				# 		arxForm.acModel.vertData[index].boneWgt2.W = (float) binaryReader.ReadByte();
				# 		break;
				# 	default:
				# 		int num7 = (int) MessageBox.Show("Not yet implemented!\n\nvertTableSize = " + (object) arxForm.acModel.vertTableSize, "Vert Read", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
				# 		return;
				# 	}
				# }
				# int num9 = fi.read(4);
				# string str3 = str1;
				# if (!(str3 == "HDMDL"))
				# {
				# 	if (str3 == "MDL")
				# 	arxForm.acModel.faceCount = num9 / 6;
				# }
				# else
				# 	arxForm.acModel.faceCount = num9 / 12;
				# arxForm.acModel.faceData = new arxForm.acFaceStruct[arxForm.acModel.faceCount];
				# for (int index = 0; index < arxForm.acModel.faceCount; ++index)
				# {
				# 	string str4 = str1;
				# 	if (!(str4 == "HDMDL"))
				# 	{
				# 	if (str4 == "MDL")
				# 	{
				# 		arxForm.acModel.faceData[index].faceIndex.Y = (float) binaryReader.ReadUInt16();
				# 		arxForm.acModel.faceData[index].faceIndex.X = (float) binaryReader.ReadUInt16();
				# 		arxForm.acModel.faceData[index].faceIndex.Z = (float) binaryReader.ReadUInt16();
				# 	}
				# 	}
				# 	else
				# 	{
				# 	arxForm.acModel.faceData[index].faceIndex.Y = (float) binaryReader.ReadUInt32();
				# 	arxForm.acModel.faceData[index].faceIndex.X = (float) binaryReader.ReadUInt32();
				# 	arxForm.acModel.faceData[index].faceIndex.Z = (float) binaryReader.ReadUInt32();
				# 	}
				# }
				# break;
			else:
				raise Exception("New switchType found")

			model_file.out_file_write('Skin Data Table\n', out_file, indent_count)
			skin_count = model_file.read_uint_32(out_file, indent_count)
			skin_table = model_file.read_numpy([
				('file_id', numpy.uint64),
				('file_type', numpy.uint32),
				('', numpy.int8),
				('', numpy.uint32),
				('bone_count', numpy.uint16),
				('', numpy.int8, 11),
				('bones', numpy.uint16, 128)
			], 286 * skin_count, out_file, indent_count)

			model_file.out_file_write(f'{skin_table}\n', out_file, indent_count)

			model_file.read_str(8, out_file, indent_count)
			model_file.out_file_write('Model Scale?\n', out_file, indent_count)
			model_file.read_float_32(out_file, indent_count)  # model scale? (possibly not)
			model_file.out_file_write('Material Table\n', out_file, indent_count)
			material_count = model_file.read_uint_32(out_file, indent_count)
			material_table = model_file.read_numpy([
				('', numpy.uint16),
				('file_id', numpy.uint64)
			], 10 * material_count, out_file, indent_count)

			model_file.out_file_write(f'{material_table}\n', out_file, indent_count)
			self.materials = material_table['file_id']

			model_file.read_rest(out_file, indent_count)

		else:
			raise Exception("Error reading model file!")
