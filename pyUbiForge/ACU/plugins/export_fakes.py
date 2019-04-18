from pyUbiForge.misc import mesh
from pyUbiForge.misc.plugins import BasePlugin
from pyUbiForge.ACU.type_readers.fakes import Reader as Fakes
from pyUbiForge.ACU.type_readers.visual import Reader as Visual
from pyUbiForge.ACU.type_readers.lod_selector import Reader as LODSelector
from pyUbiForge.ACU.type_readers.mesh_instance_data import Reader as MeshInstanceData
from typing import Union, List, Dict
import numpy


class Plugin(BasePlugin):
	plugin_name = 'Export Fakes'
	plugin_level = 4
	file_type = 'C69A7F31'
	_options = [
		{
			"Export Method": 'Wavefront (.obj)'
		},
		{
			"Texture Type": 'DirectDraw Surface (.dds)'
		}
	]

	def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: Union[List[dict], None] = None):
		if options is not None:
			self._options = options     # should do some validation here

		# TODO add select directory option
		save_folder = py_ubi_forge.CONFIG.get('dumpFolder', 'output')

		data = py_ubi_forge.temp_files(file_id, forge_file_name, datafile_id)
		if data is None:
			py_ubi_forge.log.warn(__name__, f"Failed to find file {file_id:016X}")
			return
		fakes_name = data.file_name
		fakes: Fakes = py_ubi_forge.read_file(data.file)

		if self._options[0]["Export Method"] == 'Wavefront (.obj)':
			obj_handler = mesh.ObjMtl(py_ubi_forge, fakes_name, save_folder)
			for fake in fakes.fakes + fakes.near_fakes:
				entity = fake.entity
				if entity is None:
					py_ubi_forge.log.warn(__name__, f"Failed reading file {data.file_name} {data.file_id:016X}")
					continue
				for nested_file in entity.nested_files:
					if nested_file.file_type == 'EC658D29':  # visual
						nested_file: Visual
						if '01437462' in nested_file.nested_files.keys():  # LOD selector
							lod_selector: LODSelector = nested_file.nested_files['01437462']
							mesh_instance_data: MeshInstanceData = lod_selector.lod[0]
						elif '536E963B' in nested_file.nested_files.keys():  # Mesh instance
							mesh_instance_data: MeshInstanceData = nested_file.nested_files['536E963B']
						else:
							py_ubi_forge.log.warn(__name__, f"Could not find mesh instance data for {data.file_name} {data.file_id:016X}")
							continue
						if mesh_instance_data is None:
							py_ubi_forge.log.warn(__name__, f"Failed to find file {data.file_name}")
							continue
						model_data = py_ubi_forge.temp_files(mesh_instance_data.mesh_id)
						if model_data is None:
							py_ubi_forge.log.warn(__name__, f"Failed to find file {mesh_instance_data.mesh_id:016X}")
							continue
						model: mesh.BaseModel = py_ubi_forge.read_file(model_data.file)
						if model is None or model.vertices is None:
							py_ubi_forge.log.warn(__name__, f"Failed reading model file {model_data.file_name} {model_data.file_id:016X}")
							continue
						transform = entity.transformation_matrix
						if len(mesh_instance_data.transformation_matrix) == 0:
							obj_handler.export(model, model_data.file_name, transform)
						else:
							for trm in mesh_instance_data.transformation_matrix:
								obj_handler.export(model, model_data.file_name, numpy.matmul(transform, trm))
						py_ubi_forge.log.info(__name__, f'Exported {model_data.file_name}')
			obj_handler.save_and_close()
			py_ubi_forge.log.info(__name__, f'Finished exporting {fakes_name}.obj')

		# elif self._options[0]["Export Method"] == 'Collada (.dae)':
		# 	obj_handler = mesh.Collada(py_ubi_forge, model_name, save_folder)
		# 	obj_handler.export(file_id, forge_file_name, datafile_id)
		# 	obj_handler.save_and_close()
		# 	py_ubi_forge.log.info(__name__, f'Exported {file_id:016X}')
		#
		# elif self._options[0]["Export Method"] == 'Send to Blender (experimental)':
		# 	model: mesh.BaseModel = py_ubi_forge.read_file(data.file)
		# 	if model is not None:
		# 		c = Client(('localhost', 6163))
		# 		for mesh_index, m in enumerate(model.meshes):
		# 			c.send({
		# 				'type': 'MESH',
		# 				'verts': tuple(tuple(vert) for vert in model.vertices),
		# 				'faces': tuple(tuple(face) for face in model.faces[mesh_index][:m['face_count']])
		# 			})

	def options(self, options: Union[List[dict], None]) -> Union[Dict[str, dict], None]:
		if options is None or (isinstance(options, list) and len(options) == 0):
			formats = [
				'Wavefront (.obj)',
				# 'Collada (.dae)',
				# 'Send to Blender (experimental)'
			]
			formats.remove(self._options[0]["Export Method"])
			formats.insert(0, self._options[0]["Export Method"])
			return {
				"Export Method": {
					"type": "select",
					"options": formats
				}
			}
		elif isinstance(options, list):
			if len(options) == 1:
				if options[0]["Export Method"] in ('Wavefront (.obj)', 'Collada (.dae)'):
					return {
						"Texture Type": {
							"type": "select",
							"options": [
								'DirectDraw Surface (.dds)'
							]
						}
					}
				else:
					self._options = options

			elif len(options) == 2:
				self._options = options
