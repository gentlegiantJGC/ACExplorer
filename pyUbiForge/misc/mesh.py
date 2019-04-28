import os
import logging
import shutil
import numpy
from concurrent.futures import ThreadPoolExecutor
import urllib.parse
from typing import Union, List
from pyUbiForge.misc import texture
import pyUbiForge


class BaseModel:
	_name = 'unknown'
	_vertices = None
	_texture_vertices = None
	_normals = None
	_faces = None
	_meshes = None
	_materials = None
	_bones = None

	@property
	def name(self) -> str:
		return self._name

	@property
	def vertices(self) -> numpy.ndarray:
		return self._vertices

	@property
	def texture_vertices(self) -> numpy.ndarray:
		return self._texture_vertices

	@property
	def normals(self) -> numpy.ndarray:
		return self._normals

	@property
	def faces(self) -> List[numpy.ndarray]:
		return self._faces

	@property
	def meshes(self) -> numpy.ndarray:
		return self._meshes

	@property
	def materials(self) -> numpy.ndarray:
		return self._materials

	@property
	def bones(self):
		return self._bones


class ObjMtl:
	"""This is a handler to export to the OBJ format with and MTL file for materials
	This model exporter works by writing the mesh data for each mesh directly to the file as it is given it. (using the .export method).
	These models should be pre-manipulated as the values are directly written.
	While this is being done the materials are saved to a buffer.
	When the .save_and_close method is called these materials are written to the mtl file.
	"""
	def __init__(self, model_name: str, save_folder: str):
		self.model_name = model_name
		self.save_folder = save_folder
		self.vertex_count = 0   # the number of vertices that have been processed. Used to calculate the vertex offset
		self.mtl_handler = MaterialHandler()      # used when generating the .mtl file
		self._group_name = {}   # used for getting a unique name for each model
		self.missing_no_exported = False

		# the obj file object
		if not os.path.isdir(self.save_folder):
			os.makedirs(self.save_folder)
		self._obj = open(f'{self.save_folder}{os.sep}{self.model_name}.obj', 'w')
		self._obj.write('#Wavefront Object File\n#Exported by ACExplorer, written by gentlegiantJGC, based on code from ARchive_neXt\n\n')
		self._obj.write(f'mtllib ./{self.model_name}.mtl\n')

	def group_name(self, name: str) -> str:
		"""
		Each model in the obj needs to have a unique name. When this is called a unique name will be returned
		:return: '{self.name}_{int}'
		"""
		if name not in self._group_name:
			self._group_name[name] = -1
		self._group_name[name] += 1
		return f'{name}_{self._group_name[name]}'

	def export(self, model: BaseModel, model_name: str, transformation_matrix: Union[List[numpy.ndarray], numpy.ndarray] = None) -> None:
		"""
		when called will export the currently loaded mesh to the obj file
		when finished will reset all the mesh variables so that things do not persist
		:return: None
		"""
		if isinstance(transformation_matrix, numpy.ndarray) and transformation_matrix.shape == (4, 4):
			vertices = numpy.vstack((model.vertices.transpose(), numpy.ones((1, model.vertices.shape[0]))))
			# vertices[:3, :] *= 0.001
			vertices = numpy.dot(transformation_matrix, vertices)[:3, :].transpose()
		else:
			vertices = model.vertices
		# write vertices
		self._obj.write(('v {} {} {}\n' * vertices.shape[0]).format(*vertices.ravel().round(6)))
		self._obj.write(f'# {len(model.vertices)} vertices\n\n')

		# write texture coords
		self._obj.write(('vt {} {}\n' * model.texture_vertices.shape[0]).format(*model.texture_vertices.ravel().round(6)))
		self._obj.write(f'# {len(model.texture_vertices)} texture coordinates\n\n')

		# write faces
		for mesh_index, mesh in enumerate(model.meshes):
			self._obj.write(f'g {self.group_name(model_name)}\nusemtl {self.mtl_handler.get(model.materials[mesh_index]).name}\n')
			self._obj.write(('f {}/{} {}/{} {}/{}\n' * mesh['face_count']).format(*numpy.repeat(model.faces[mesh_index][:mesh['face_count']], 2).astype(numpy.int_) + self.vertex_count + 1))
			self._obj.write(f'# {mesh["face_count"]} faces\n\n')

		self.vertex_count += len(model.vertices)

	def save_and_close(self) -> None:
		"""
		when called will create the mtl file and write its contents
		when finished will close both mtl and self._obj
		:return:
		"""
		if not os.path.isdir(self.save_folder):
			os.makedirs(self.save_folder)
		mtl = open(f'{self.save_folder}{os.sep}{self.model_name}.mtl', 'w')
		mtl.write('# Material Library\n#Exported by ACExplorer, written by gentlegiantJGC, based on code from ARchive_neXt\n\n')

		with ThreadPoolExecutor(max_workers=10) as executor:
			fild_ids = [
				file_id
				for
				material in self.mtl_handler.materials.values()
				if not material.missing_no for
				map_type, file_id in [
					['map_Kd', material.diffuse],
					['map_d', material.diffuse],
					['map_Ks', material.specular],
					['map_bump', material.normal],
					['disp', material.height]
				]
				if file_id is not None
			]
			materials = list(executor.map(
				texture.export_dds,
				fild_ids,
				[self.save_folder] * len(fild_ids)
			))

		material_counter = 0
		for material in self.mtl_handler.materials.values():
			mtl.write(f'newmtl {material.name}\n')
			mtl.write('Ka 1.000 1.000 1.000\nKd 1.000 1.000 1.000\nKs 0.000 0.000 0.000\nNs 0.000\n')

			if material.missing_no:
				mtl.write(f"map_Kd {os.path.basename(pyUbiForge.CONFIG.get('missingNo', 'resources/missingNo.png'))}\n")
				self.export_missing_no()
			else:
				for map_type, file_id in [
											['map_Kd', material.diffuse],
											['map_d', material.diffuse],
											['map_Ks', material.specular],
											['map_bump', material.normal],
											['disp', material.height]
										]:
					if file_id is not None:
						image_path = materials[material_counter]
						material_counter += 1
						if image_path is None:
							mtl.write(f"{map_type} {os.path.basename(pyUbiForge.CONFIG.get('missingNo', 'resources/missingNo.png'))}\n")
							self.export_missing_no()
						else:
							mtl.write(f'{map_type} {os.path.basename(image_path)}\n')
			mtl.write('\n')
		mtl.close()
		self._obj.close()

	def export_missing_no(self) -> None:
		"""
		Call this to copy over the missingNo image if it has not already been copied over
		:return: None
		"""
		if not self.missing_no_exported:
			self.missing_no_exported = True
			shutil.copy(pyUbiForge.CONFIG.get('missingNo', 'resources/missingNo.png'), self.save_folder)


def plaintext_array(array):
	numpy.set_printoptions(threshold=numpy.inf)
	return numpy.array2string(array.ravel(), formatter={'float': lambda x: ('%.6f' % x).rstrip('0').rstrip('.')}, separator=' ', max_line_width=numpy.inf)[1:-1]


class Collada:
	"""This is a handler for exporting to the COLLADA .dae format.
	The handling for this format is quite a bit different to that of the OBJ format.
	The format holds a list of all the models but only one of each unique model.
	There is then another list of all the instances of the models including transformation matrix for each.
	This should make the file size a lot smaller.
	First use .is_exported to check if the model id has been exported.
		If it hasn't been then read the model file
	"""
	def __init__(self, model_name: str, save_folder: str):
		self.model_name = model_name
		self.save_folder = save_folder
		self._models_exported = {}
		self._mtl_handler = MaterialHandler()      # used when generating the .mtl file
		self._group_name = {}   # used for getting a unique name for each model
		self._library_visual_scenes = []
		self.missing_no_exported = False

		# the obj file object
		if not os.path.isdir(self.save_folder):
			os.makedirs(self.save_folder)
		self._dae = open(f'{self.save_folder}{os.sep}{self.model_name}.dae', 'w')
		self._dae.write('''<?xml version="1.0" encoding="utf-8"?>
<COLLADA xmlns="http://www.collada.org/2005/11/COLLADASchema" version="1.4.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<library_geometries>
''')

	def group_name(self, name: str) -> str:
		"""
		Each model in the obj needs to have a unique name. When this is called a unique name will be returned
		:return: '{self.name}_{int}'
		"""
		if name not in self._group_name:
			self._group_name[name] = -1
		self._group_name[name] += 1
		return f'{name}_{self._group_name[name]}'

	def is_exported(self, file_id: int):
		return file_id in self._models_exported

	def export(self, model_file_id: int, forge_file_name: str = None, datafile_id: int = None, transformation_matrix: numpy.ndarray = None) -> None:
		"""
		when called will load and export the mesh if it hasn't been
		:return: None
		"""

		if not self.is_exported(model_file_id):
			data = pyUbiForge.temp_files(model_file_id, forge_file_name, datafile_id)
			if data is None:
				logging.warning(f"Failed to find file {model_file_id:016X}")
				return
			model = pyUbiForge.read_file(data.file)
			if model is None:  # sometimes reading the model fails
				return
			self._models_exported[model_file_id] = []

			# write models
			for mesh_index, mesh in enumerate(model.meshes):
				faces = model.faces[mesh_index][:mesh['face_count']].ravel()
				new_value_slice, faces = numpy.unique(faces, return_inverse=True)
				vertices = model.vertices[new_value_slice]
				texture_vertices = model.texture_vertices[new_value_slice]

				geometry_id = f'{model_file_id}-mesh-{mesh_index}'
				model_name = f'{data.file_name}-{mesh_index}'
				material_name = f'{self._mtl_handler.get(model.materials[mesh_index]).name}-material'
				self._models_exported[model_file_id].append([geometry_id, model_name, material_name])

				self._dae.write(f'''		<geometry id="{model_file_id}-mesh-{mesh_index}" name="{model_name}">
			<mesh>
				<source id="{model_file_id}-mesh-positions-{mesh_index}">
					<float_array id="{model_file_id}-mesh-positions-array-{mesh_index}" count="{vertices.size}">{plaintext_array(vertices)}</float_array>
					<technique_common>
						<accessor source="#{model_file_id}-mesh-positions-array-{mesh_index}" count="{len(vertices)}" stride="3">
							<param name="X" type="float"/>
							<param name="Y" type="float"/>
							<param name="Z" type="float"/>
						</accessor>
					</technique_common>
				</source>
''')
				if model.normals is not None:
					normals = model.normals[new_value_slice]
					self._dae.write(f'''				<source id="{model_file_id}-mesh-normals-{mesh_index}">
					<float_array id="{model_file_id}-mesh-normals-array-{mesh_index}" count="{normals.size}">{plaintext_array(normals)}</float_array>
					<technique_common>
						<accessor source="#{model_file_id}-mesh-normals-array-{mesh_index}" count="{len(normals)}" stride="3">
							<param name="X" type="float"/>
							<param name="Y" type="float"/>
							<param name="Z" type="float"/>
						</accessor>
					</technique_common>
				</source>
''')
				self._dae.write(f'''				<source id="{model_file_id}-mesh-map-0-{mesh_index}">
					<float_array id="{model_file_id}-mesh-map-0-array-{mesh_index}" count="{texture_vertices.size}">{plaintext_array(texture_vertices)}</float_array>
					<technique_common>
						<accessor source="#{model_file_id}-mesh-map-0-array-{mesh_index}" count="{len(texture_vertices)}" stride="2">
							<param name="S" type="float"/>
							<param name="T" type="float"/>
						</accessor>
					</technique_common>
				</source>
				<vertices id="{model_file_id}-mesh-vertices-{mesh_index}">
					<input semantic="POSITION" source="#{model_file_id}-mesh-positions-{mesh_index}"/>
				</vertices>
				<triangles material="{material_name}" count="{len(faces)}">
					<input semantic="VERTEX" source="#{model_file_id}-mesh-vertices-{mesh_index}" offset="0"/>
''')
				if model.normals is not None:
					self._dae.write(f'''					<input semantic="NORMAL" source="#{model_file_id}-mesh-normals-{mesh_index}" offset="0"/>
''')
				self._dae.write(f'''					<input semantic="TEXCOORD" source="#{model_file_id}-mesh-map-0-{mesh_index}" offset="0" set="0"/>
					<p>{plaintext_array(faces)}</p>
				</triangles>
			</mesh>
		</geometry>
''')

		if transformation_matrix is None:
			transformation_matrix = numpy.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
		for geometry_id, model_name, material_name in self._models_exported[model_file_id]:
			self._library_visual_scenes.append(f'''			<node id="{model_name}" name="{model_name}" type="NODE">
				<matrix sid="transform">{plaintext_array(transformation_matrix)}</matrix>
				<instance_geometry url="#{geometry_id}" name="{model_name}">
					<bind_material>
						<technique_common>
							<instance_material symbol="{material_name}" target="#{material_name}"/>
						</technique_common>
					</bind_material>
				</instance_geometry>
			</node>
''')

	def save_and_close(self) -> None:
		"""
		when called will write the textures, materials and scene data
		when finished will close self._dae
		:return:
		"""

		library_materials = []
		library_effects = []
		library_images = []

		self._dae.write('''	</library_geometries>
''')

		self._dae.write(f'''	<library_visual_scenes>
		<visual_scene id="Scene" name="Scene">
{''.join(self._library_visual_scenes)}		</visual_scene>
	</library_visual_scenes>
''')

		for material in self._mtl_handler.materials.values():
			image_path = None
			material_name = material.name
			if material.missing_no:
				image_path = os.path.basename(pyUbiForge.CONFIG.get('missingNo', 'resources/missingNo.png'))
				self.export_missing_no()
			else:
				for map_type, file_id in [
					['diffuse', material.diffuse]#,
					# ['map_d', material.diffuse],
					# ['map_Ks', material.specular],
					# ['map_bump', material.normal],
					# ['disp', material.height]
				]:
					if file_id is None:
						continue
					image_path = os.path.basename(texture.export_dds(file_id, self.save_folder))
					if image_path is None:
						image_path = os.path.basename(pyUbiForge.CONFIG.get('missingNo', 'resources/missingNo.png'))
						self.export_missing_no()
					library_images.append(f'''		<image id="{material_name}-{map_type}" name="{material_name}">
			<init_from>{urllib.parse.quote(image_path)}</init_from>
		</image>
''')
			
			library_effects.append(f'''		<effect id="{material_name}-effect">
			<profile_COMMON>
				<newparam sid="{material_name}-surface">
					<surface type="2D">
						<init_from>{material_name}-diffuse</init_from>
					</surface>
				</newparam>
				<newparam sid="{material_name}-sampler">
					<sampler2D>
						<source>{material_name}-surface</source>
					</sampler2D>
				</newparam>
				<technique sid="common">
					<phong>
						<emission>
							<color sid="emission">0 0 0 1</color>
						</emission>
						<ambient>
							<color sid="ambient">0 0 0 1</color>
						</ambient>
						<diffuse>
							<texture texture="{material_name}-sampler"/>
						</diffuse>
						<specular>
							<color sid="specular">0.5 0.5 0.5 1</color>
						</specular>
						<shininess>
							<float sid="shininess">50</float>
						</shininess>
						<index_of_refraction>
							<float sid="index_of_refraction">1</float>
						</index_of_refraction>
					</phong>
				</technique>
			</profile_COMMON>
		</effect>
''')

			library_materials.append(f'''		<material id="{material_name}-material" name="{material_name}">
			<instance_effect url="#{material_name}-effect"/>
		</material>
''')

		self._dae.write(f'''	<library_images>
{''.join(library_images)}	</library_images>
''')

		self._dae.write(f'''	<library_effects>
{''.join(library_effects)}	</library_effects>
''')

		self._dae.write(f'''	<library_materials>
{''.join(library_materials)}	</library_materials>
''')

		self._dae.write('''	<scene>
		<instance_visual_scene url="#Scene"/>
	</scene>
''')
		self._dae.write('</COLLADA>')

		self._dae.close()

	def export_missing_no(self) -> None:
		"""
		Call this to copy over the missingNo image if it has not already been copied over
		:return: None
		"""
		if not self.missing_no_exported:
			self.missing_no_exported = True
			shutil.copy(pyUbiForge.CONFIG.get('missingNo', 'resources/missingNo.png'), self.save_folder)


class MaterialHandler:
	def __init__(self):
		self.materials = {}
		self.name = 'Unknown'

	def get(self, file_id: int):
		if file_id not in self.materials:
			self.materials[file_id] = pyUbiForge.game_functions.get_material_ids(file_id)
		return self.materials[file_id]
