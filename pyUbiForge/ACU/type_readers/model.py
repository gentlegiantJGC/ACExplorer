from pyUbiForge.misc.mesh import BaseModel
from pyUbiForge.misc.file_readers import BaseReader
from pyUbiForge.misc.file_object import FileObjectDataWrapper
import numpy
import pyUbiForge
import logging


class Reader(BaseModel, BaseReader):
	file_type = '415D9568'

	def __init__(self, model_file: FileObjectDataWrapper):
		BaseModel.__init__(self)

		model_file.out_file_write('\n')
		model_file.read_bytes(1)  # skip an empty byte
		self.type = model_file.read_bytes(4)
		model_file.read_bytes(1)
		a_count = model_file.read_uint_32()
		for a in range(a_count*2):
			check = model_file.read_uint_8()
			while check == 3:
				check = model_file.read_uint_8()
			model_file.read_bytes(1)
			pyUbiForge.read_file.get_data_recursive(model_file)
		if a_count > 0:
			model_file.read_bytes(1)

		bone_count = model_file.read_uint_32()
		self._bones = []
		for _ in range(bone_count):
			self._bones.append(pyUbiForge.read_file.get_data_recursive(model_file))

		self.bounding_box = model_file.read_numpy(numpy.float32, 32).reshape(2, 4)
		model_file.out_file_write(f'{self.bounding_box}\n')

		model_file.read_bytes(1)

		model_file.read_id()
		if model_file.read_type() == "FC9E1595":  # this part should get moved to a different file technically
			model_file.read_bytes(4)
			model_file.out_file_write('Typeswitch\n')
			self.type_switch = model_file.read_bytes(1)
			use_blocks = 0
			if self.type_switch == b'\x00':
				model_file.read_id()
				model_file.read_type()
				model_file.read_bytes(5)
				model_file.out_file_write('Vert table width\n')
				vert_table_width = model_file.read_uint_32()
				mesh_face_block_sum = model_file.read_uint_32() # = sum(mesh_face_blocks)
				bounding_box2 = model_file.read_numpy(numpy.float32, 24).reshape(2, 3)
				mesh_face_block_count = model_file.read_uint_32()
				shadow_face_block_count = model_file.read_uint_32()
				model_file.out_file_write('Mesh Face Blocks\n')
				mesh_face_blocks = model_file.read_numpy(numpy.uint32, 4*mesh_face_block_count)
				shadow_face_blocks = model_file.read_numpy(numpy.uint32, 4*shadow_face_block_count)
				model_file.read_uint_32()
				use_blocks = model_file.read_uint_8()    # use blocks?
				model_file.out_file_write('\nVert table\n')
				vert_table_length = model_file.read_uint_32()
				self.vert_count = vert_table_length / vert_table_width

				if vert_table_width == 16:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('', numpy.int16, 2),  # not sure what this is
						('vt', numpy.int16, 2)
					], vert_table_length)

				elif vert_table_width == 20:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16),  # not sure what this is
						('vt', numpy.int16, 2)
					], vert_table_length)

				elif vert_table_width == 24:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2)
					], vert_table_length)

				elif vert_table_width == 28:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('', numpy.int16, 2),  # not sure what this is
					], vert_table_length)

				elif vert_table_width == 32:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('bn', numpy.uint8, 4),
						('bw', numpy.uint8, 4)
					], vert_table_length)

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
					], vert_table_length)

				elif vert_table_width == 40:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('bn', numpy.uint8, 8),
						('bw', numpy.uint8, 8)
					], vert_table_length)

				elif vert_table_width == 48:
					vert_table = model_file.read_numpy([
						('v', numpy.int16, 3),
						('sc', numpy.int16),
						('n', numpy.int16, 3),
						('', numpy.int16, 3),  # not sure what this is
						('vt', numpy.int16, 2),
						('', numpy.int16, 2),  # not sure what this is
						('bn', numpy.uint8, 8),
						('bw', numpy.uint8, 8),
						('', numpy.int16, 2),  # not sure what this is
					], vert_table_length)
				else:
					logging.warning(f'Not yet implemented!\n\nvertTableWidth = {vert_table_width}')
					raise Exception()

				self._vertices = vert_table['v'].astype(numpy.float) * numpy.sign(vert_table['sc'].reshape(-1, 1)) / 2 ** 15
				# self._vertices *= numpy.sum(bounding_box2, 0) / numpy.amax(self.vertices, 0)

				self._texture_vertices = vert_table['vt'].astype(numpy.float) / 2048.0
				self._texture_vertices[:, 1] *= -1
				if 'n' in vert_table.dtype.names:
					self._normals = vert_table['n'].astype(numpy.float)
				if 'bn' in vert_table.dtype.names:
					self.bone_numbers = vert_table['bn']
					self.bone_weights = vert_table['bw']
				else:
					self.bone_number = None
				self.vert_table = vert_table

				model_file.out_file_write('Face table\n')
				face_table_length = model_file.read_uint_32()
				self._faces = model_file.read_numpy(numpy.uint16, face_table_length).reshape(-1, 3)
				# self._faces = numpy.split(face_table, numpy.cumsum(mesh_face_blocks * 64)[:-1])
				#
				#
				# mesh_face_blocks_x64 = numpy.cumsum(mesh_face_blocks * 64)
				# mesh_face_blocks_x64[-1] =
				# mesh_face_blocks[-1] =* 64 * 6 == face_table_length:
				# 	self._faces = [face_table[64*mesh_face_blocks[index-1]:64*block_count] for index, block_count in enumerate(mesh_face_blocks)]
				# self._faces = [face_table[:64 * block_count] if index==0 else face_table[64*mesh_face_blocks[index-1]:64*block_count] for index, block_count in enumerate(mesh_face_blocks)]

				for _ in range(3):
					count = model_file.read_uint_32()
					model_file.read_bytes(count)

			model_file.read_id()
			model_file.read_type()
			model_file.read_bytes(3)
			model_file.out_file_write('Mesh Table\n')
			mesh_count = model_file.read_uint_32()
			self._meshes = model_file.read_numpy([
				('file_id', numpy.uint64),
				('file_type', numpy.uint32),
				('verts_used', numpy.uint32),  # this is not always perfect
				('', numpy.uint32),
				('vert_count', numpy.uint32),
				('faces_used_x3', numpy.uint32),
				('face_count', numpy.uint32),
				('', numpy.uint32)
			], 36 * mesh_count)

			if self._faces is not None:
				if use_blocks == 1:
					self._faces = numpy.split(self._faces, numpy.cumsum(mesh_face_blocks * 64)[:-1])
					for index in range(len(self._faces)):
						self._faces[index] = self._faces[index][:self.meshes['face_count'][index]]  # strip the end of the block
						if index >= 1:
							self._faces[index] += self._faces[index-1].max() + 1  # add the vertex offset (each block starts from 0)
				else:
					faces = self._faces
					self._faces = []
					for faces_used_x3, face_count, verts_used in zip(self.meshes['faces_used_x3'], self.meshes['face_count'], self.meshes['verts_used']):
						self._faces.append(faces[int(faces_used_x3/3):int(faces_used_x3/3)+face_count] + verts_used)

			model_file.out_file_write('Shadow Table\n')
			shadow_count = model_file.read_uint_32()
			shadow_table = model_file.read_numpy([
				('file_id', numpy.uint64),
				('file_type', numpy.uint32),
				('X', numpy.uint32),
				('', numpy.uint32),
				('Y', numpy.uint32),
				('Z', numpy.uint32),
				('W', numpy.uint32),
				('', numpy.uint32),
			], 36 * shadow_count)

			model_file.out_file_write(f'{shadow_table}\n')

			for index in range(2):
				count = model_file.read_uint_32()
				model_file.indent()
				model_file.read_bytes(count)
				model_file.indent(-1)

			model_file.out_file_write('Skin Data Table\n')
			skin_count = model_file.read_uint_32()
			skin_table = model_file.read_numpy([
				('file_id', numpy.uint64),
				('file_type', numpy.uint32),
				('', numpy.int8),
				('', numpy.uint32),
				('bone_count', numpy.uint16),
				('', numpy.int8, 11),
				('bones', numpy.uint16, 128)
			], 286 * skin_count)

			model_file.out_file_write(f'{skin_table}\n')

			model_file.read_bytes(8)
			model_file.out_file_write('Model Scale?\n')
			model_scale = model_file.read_float_32()  # model scale? (looks to be the magnitude of sc in the vert table)
			self._vertices *= model_scale
			model_file.out_file_write('Material Table\n')
			material_count = model_file.read_uint_32()
			material_table = model_file.read_numpy([
				('', numpy.uint16),
				('file_id', numpy.uint64)
			], 10 * material_count)

			model_file.out_file_write(f'{material_table}\n')
			self._materials = material_table['file_id']

			model_file.read_rest()

		else:
			raise Exception("Error reading model file!")
