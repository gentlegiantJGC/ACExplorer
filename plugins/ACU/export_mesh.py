from pyUbiForge.misc import mesh
from plugins import BasePlugin
from typing import Union, List, Dict
from multiprocessing.connection import Client
from PIL import Image
import numpy
import pyUbiForge
import logging
import os
import json


class Plugin(BasePlugin):
	plugin_name = 'Export Mesh'
	plugin_level = 4
	file_type = '415D9568'
	_options = [
		{
			"Export Method": 'Wavefront (.obj)'
		},
		{
			"Texture Type": 'DirectDraw Surface (.dds)'
		}
	]

	def run(self, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: Union[List[dict], None] = None):
		if options is not None:
			self._options = options     # should do some validation here

		# TODO add select directory option
		save_folder = pyUbiForge.CONFIG.get('dumpFolder', 'output')

		data = pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)
		if data is None:
			logging.warning(f"Failed to find file {file_id:016X}")
			return
		model_name = data.file_name

		if self._options[0]["Export Method"] == 'Wavefront (.obj)':
			model: mesh.BaseModel = pyUbiForge.read_file(data.file)
			if model is not None:
				obj_handler = mesh.ObjMtl(model_name, save_folder)
				obj_handler.export(model, model_name)
				obj_handler.save_and_close()
				logging.info(f'Exported {file_id:016X}')
			else:
				logging.warning(f'Failed to export {file_id:016X}')

		elif self._options[0]["Export Method"] == 'Collada (.dae)':
			obj_handler = mesh.Collada(model_name, save_folder)
			obj_handler.export(file_id, forge_file_name, datafile_id)
			obj_handler.save_and_close()
			logging.info(f'Exported {file_id:016X}')

		elif self._options[0]["Export Method"] == 'Send to Blender (experimental)':
			if os.path.isfile(os.path.join(os.path.dirname(__file__), 'bone_hierarchy.json')):
				with open(os.path.join(os.path.dirname(__file__), 'bone_hierarchy.json')) as f:
					bone_hierarchy: Dict[str, str] = json.load(f)
			else:
				bone_hierarchy: Dict[str, str] = {}

			model: mesh.BaseModel = pyUbiForge.read_file(data.file)
			if model is not None:
				c = Client(('localhost', 6163))
				faces = []
				for mesh_index, m in enumerate(model.meshes):
					faces.append(tuple(model.faces[mesh_index][:m['face_count']]))

				trms = {}
				# collect the correct transformation matrix for each bone
				for bone in model.bones:
					trms[bone.bone_id] = [numpy.linalg.inv(bone.transformation_matrix), None]

				# collect parents
				for bone in model.bones:
					if bone.bone_id in bone_hierarchy:
						parent_bone_id = next((bid for bid in bone_hierarchy[bone.bone_id] if bid in trms), None)
						if parent_bone_id is not None:
							trms[bone.bone_id][1] = pyUbiForge.game_functions.file_types.get(parent_bone_id, parent_bone_id)

				bone_weights = []
				for bone_indexs, bone_weights_ in zip(model.bone_numbers, model.bone_weights):
					vertex_weights = []
					for bone_index, bone_weight in zip(bone_indexs, bone_weights_):
						if bone_weight != 0:
							vertex_weights.append(
								[pyUbiForge.game_functions.file_types.get(model.bones[bone_index].bone_id, model.bones[bone_index].bone_id), bone_weight]
							)
					bone_weights.append(vertex_weights)

				# print(bone_weights)

				c.send({
					'type': 'MESH',
					'verts': tuple(model.vertices),
					'tvers': tuple(model.texture_vertices),
					'faces': faces,
					'bone_id_trm': {pyUbiForge.game_functions.file_types.get(bone_id, bone_id): mats for bone_id, mats in trms.items()},
					'bone_weights': bone_weights
				})

	def options(self, options: Union[List[dict], None]) -> Union[Dict[str, dict], None]:
		if options is None or (isinstance(options, list) and len(options) == 0):
			formats = [
				'Wavefront (.obj)',
				'Collada (.dae)',
				'Send to Blender (experimental)'
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
