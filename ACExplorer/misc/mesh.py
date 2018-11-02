import os
import shutil


class ObjMtl(object):
	def __init__(self, app, model_name):
		self.app = app
		self.model_name = model_name
		self.vertex_count = 0   # the number of vertices that have been processed. Used to calculate the vertex offset
		self.mtl_handler = MaterialHandler(self.app)      # used when generating the .mtl file
		self._group_name = {}   # used for getting a unique name for each model
		self.missing_no_exported = False

		# the obj file object
		self._obj = open('{}{}{}.obj'.format(self.app.CONFIG['dumpFolder'], os.sep, self.model_name), 'w')
		self._obj.write('#Wavefront Object File\n#Exported by ACExplorer, written by gentlegiantJGC, based on code from ARchive_neXt\n\n')
		self._obj.write('mtllib ./{}.mtl\n'.format(self.model_name))

	def group_name(self, name):
		"""
		Each model in the obj needs to have a unique name. When this is called a unique name will be returned
		:return: '{self.name}_{int}'
		"""
		if name not in self._group_name:
			self._group_name[name] = -1
		self._group_name[name] += 1
		return '{}_{}'.format(name, self._group_name[name])

	def export(self, model):
		"""
		when called will export the currently loaded mesh to the obj file
		when finished will reset all the mesh variables so that things do not persist
		:return: None
		"""
		# write vertices
		self._obj.write(''.join(['v {} {} {}\n'.format(*vertex) for vertex in model.vertices.round(6)]))
		self._obj.write('# {} vertices\n\n'.format(len(model.vertices)))

		# write texture coords
		self._obj.write(''.join(['vt {} {}\n'.format(*vertex) for vertex in model.texture_vertices.round(6)]))
		self._obj.write('# {} texture coordinates\n\n'.format(len(model.texture_vertices)))

		# write faces
		for mesh_index, mesh in enumerate(model.meshes):
			self._obj.write('g {}\n'.format(self.group_name(model.name)))
			self._obj.write('usemtl {}\n'.format(self.mtl_handler.get(model.materials[mesh_index]).name))
			self._obj.write(''.join(['f {0}/{0} {1}/{1} {2}/{2}\n'.format(*face) for face in model.faces[mesh_index][:mesh['face_count']] + self.vertex_count]))
			self._obj.write('# {} faces\n\n'.format(mesh['face_count']))

		self.vertex_count += len(model.vertices)

	def save_and_close(self):
		"""
		when called will create the mtl file and write its contents
		when finished will close both mtl and self._obj
		:return:
		"""
		mtl = open('{}{}{}.mtl'.format(self.app.CONFIG['dumpFolder'], os.sep, self.model_name), 'w')
		mtl.write('# Material Library\n#Exported by ACExplorer, written by gentlegiantJGC, based on code from ARchive_neXt\n\n')
		for material in self.mtl_handler.materials.values():
			mtl.write('newmtl {}\n'.format(material.name))
			mtl.write('Ka 1.000 1.000 1.000\nKd 1.000 1.000 1.000\nKs 0.000 0.000 0.000\nNs 0.000\n')

			if material.missing_no:
				mtl.write('map_Kd {}\n'.format(os.path.basename(self.app.CONFIG['missingNo'])))
				self.export_missing_no()
			else:
				for map_type, file_id in [
											['map_Kd', material.diffuse],
											['map_d', material.diffuse],
											['map_Ks', material.specular],
											['map_bump', material.normal],
											['disp', material.height]
										]:
					if file_id is None:
						continue
					image_path = self.app.gameFunctions.export_texture(self.app, file_id)
					if image_path is None:
						mtl.write('{} {}\n'.format(map_type, os.path.basename(self.app.CONFIG['missingNo'])))
						self.export_missing_no()
					else:
						mtl.write('{} {}\n'.format(map_type, os.path.basename(image_path)))
			mtl.write('\n')
		mtl.close()
		self._obj.close()

	def export_missing_no(self):
		"""
		Call this to copy over the missingNo image if it has not already been copied over
		:return: None
		"""
		if not self.missing_no_exported:
			self.missing_no_exported = True
			shutil.copy(self.app.CONFIG['missingNo'], self.app.CONFIG['dumpFolder'])


class MaterialHandler:
	def __init__(self, app):
		self.app = app
		self.materials = {}
		self.name = 'Unknown'

	def get(self, file_id):
		if file_id not in self.materials:
			self.materials[file_id] = self.app.gameFunctions.get_material_ids(self.app, file_id)
		return self.materials[file_id]


class Model:
	def __init__(self):
		self.name = None
		self.vertices = None
		self.texture_vertices = None
		self.normals = None
		self.faces = None
		self.meshes = None
		self.materials = None