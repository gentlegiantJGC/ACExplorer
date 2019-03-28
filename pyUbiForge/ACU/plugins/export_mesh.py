from pyUbiForge.misc import mesh
from pyUbiForge.misc.plugins import BasePlugin
from typing import Union, List, Dict
from multiprocessing.connection import Client


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

	def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: Union[List[dict], None] = None):
		if options is not None:
			self._options = options     # should do some validation here

		# TODO add select directory option
		save_folder = py_ubi_forge.CONFIG.get('dumpFolder', 'output')

		data = py_ubi_forge.temp_files(file_id, forge_file_name, datafile_id)
		if data is None:
			py_ubi_forge.log.warn(__name__, f"Failed to find file {file_id:016X}")
			return
		model_name = data.file_name

		if self._options[0]["Export Method"] == 'Wavefront (.obj)':
			model: mesh.BaseModel = py_ubi_forge.read_file(data.file)
			if model is not None:
				obj_handler = mesh.ObjMtl(py_ubi_forge, model_name, save_folder)
				obj_handler.export(model, model_name)
				obj_handler.save_and_close()
				py_ubi_forge.log.info(__name__, f'Exported {file_id:016X}')
			else:
				py_ubi_forge.log.warn(__name__, f'Failed to export {file_id:016X}')

		elif self._options[0]["Export Method"] == 'Collada (.dae)':
			obj_handler = mesh.Collada(py_ubi_forge, model_name, save_folder)
			obj_handler.export(file_id, forge_file_name, datafile_id)
			obj_handler.save_and_close()
			py_ubi_forge.log.info(__name__, f'Exported {file_id:016X}')

		elif self._options[0]["Export Method"] == 'Send to Blender (experimental)':
			model: mesh.BaseModel = py_ubi_forge.read_file(data.file)
			if model is not None:
				c = Client(('localhost', 6163))
				for mesh_index, m in enumerate(model.meshes):
					c.send({
						'type': 'MESH',
						'verts': tuple(tuple(vert) for vert in model.vertices),
						'faces': tuple(tuple(face) for face in model.faces[mesh_index][:m['face_count']])
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
