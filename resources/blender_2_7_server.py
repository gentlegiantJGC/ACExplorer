from multiprocessing.connection import Listener
import threading
import bpy
import mathutils


class Server(threading.Thread):
	def __init__(self, address):
		threading.Thread.__init__(self)
		self.address = address
		self.main_thread = next(th for th in threading.enumerate() if th.__class__.__name__ == '_MainThread')
		self.stay_alive = True

	def run(self):
		serv = Listener(self.address)
		while self.main_thread.is_alive():
			client = Child(serv)
			client.start()
			while self.main_thread.is_alive() and client.is_alive():
				pass
		serv.close()


class Child(threading.Thread):
	def __init__(self, server):
		threading.Thread.__init__(self)
		self.server = server
		self.connected = False

	def run(self):
		try:
			client = self.server.accept()
		except:
			return
		self.connected = True
		while self.connected:
			try:
				msg = client.recv()
				if isinstance(msg, dict) and msg.get('type', None) == 'MESH':
					verts = msg.get('verts', [])
					tverts = msg.get('tverts', [])
					faces = msg.get('faces', [])
					mesh_data = bpy.data.meshes.new("cube_mesh_data")
					mesh_data.from_pydata(verts, [], faces)
					mesh_data.update()

					obj = bpy.data.objects.new("My_Object", mesh_data)

					scene = bpy.context.scene
					scene.objects.link(obj)
					# obj.select = True

				elif isinstance(msg, dict) and msg.get('type', None) == 'BONES':
					bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
					if bpy.ops.object.mode_set.poll():
						bpy.ops.object.mode_set(mode='OBJECT')
					bpy.ops.object.armature_add()
					armature = bpy.data.armatures[-1]

					if bpy.ops.object.mode_set.poll():
						bpy.ops.object.mode_set(mode='EDIT')

					for bone in armature.edit_bones:
						armature.edit_bones.remove(bone)

					# for bone_id, transformation_matrix in zip(msg['bone_id'], msg['mat']):
					# 	edit_bone = armature.edit_bones.new(bone_id)
					# 	edit_bone.tail = (1, 0, 0)
					#
					# 	edit_bone.matrix = mathutils.Matrix(
					# 		(
					# 			transformation_matrix[0, :],
					# 			transformation_matrix[1, :],
					# 			transformation_matrix[2, :],
					# 			transformation_matrix[3, :]
					# 		)
					# 	)
					# 	edit_bone.length = edit_bone.matrix.to_scale().length * 0.2
					#
					# 	# edit_bone2 = armature.edit_bones.new(bone_id)
					# 	# edit_bone2.tail = transformation_matrix[:3, 3]
					# 	print('imported_bone')

					for bone_id, (head_pos, tail_pos) in msg['bone_id_trm'].items():
						edit_bone = armature.edit_bones.new(bone_id)
						edit_bone.head = head_pos
						edit_bone.tail = tail_pos

						# edit_bone.matrix = mathutils.Matrix(
						# 	(
						# 		transformation_matrix[0, :],
						# 		transformation_matrix[1, :],
						# 		transformation_matrix[2, :],
						# 		transformation_matrix[3, :]
						# 	)
						# )
						# edit_bone.length = edit_bone.matrix.to_scale().length * 0.2

						# edit_bone2 = armature.edit_bones.new(bone_id)
						# edit_bone2.tail = transformation_matrix[:3, 3]
						print('imported_bone')

					if bpy.ops.object.mode_set.poll():
						bpy.ops.object.mode_set(mode='OBJECT')
					if bpy.ops.object.mode_set.poll():
						bpy.ops.object.mode_set(mode='EDIT')
					if bpy.ops.object.mode_set.poll():
						bpy.ops.object.mode_set(mode='OBJECT')

				else:
					print('{}\n{}'.format(type(msg), msg))
			except EOFError:
				self.connected = False


s = Server(('', 6163))
s.start()
