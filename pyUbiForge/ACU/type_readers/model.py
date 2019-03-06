from pyUbiForge.misc.mesh import BaseModel
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseModel, BaseReader):
	file_type = '415D9568'

	def __init__(self, py_ubi_forge, model_file, out_file, indent_count):
		BaseModel.__init__(self)

		model_file.out_file_write('\n', out_file, indent_count)
		model_file.read_str(1, out_file, indent_count)  # skip an empty byte
		self.type = model_file.read_str(4, out_file, indent_count)
		model_file.read_str(1, out_file, indent_count)
		a_count = model_file.read_uint_32(out_file, indent_count)
		for a in range(a_count*2):
			model_file.read_str(2, out_file, indent_count)
			py_ubi_forge.read_file.get_data_recursive(model_file, out_file, indent_count)
		if a_count > 0:
			model_file.read_str(1, out_file, indent_count)

		bone_count = model_file.read_uint_32(out_file, indent_count)
		self.bones = []
		for _ in range(bone_count):
			self.bones.append(py_ubi_forge.read_file.get_data_recursive(model_file, out_file, indent_count))

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
					py_ubi_forge.log.warn(__name__, f'Not yet implemented!\n\nvertTableWidth = {vert_table_width}')
					raise Exception()

				model_file.out_file_write(f'{vert_table}\n', out_file, indent_count)

				self.vertices = vert_table['v'].astype(numpy.float) / vert_table['sc'].reshape(-1, 1).astype(numpy.float)
				# self.vertices *= numpy.sum(bounding_box2, 0) / numpy.amax(self.vertices, 0)
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

			if self.faces is not None:
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
