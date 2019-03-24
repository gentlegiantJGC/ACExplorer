from pyUbiForge.misc import mesh
from pyUbiForge.misc.plugins import BasePlugin
from typing import Union


class Plugin(BasePlugin):
	plugin_name = 'Export COLLADA'
	plugin_level = 4
	file_type = '415D9568'

	def run(self, py_ubi_forge, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: list = None):
		# TODO add select directory option
		save_folder = py_ubi_forge.CONFIG.get('dumpFolder', 'output')

		data = py_ubi_forge.temp_files(file_id, forge_file_name, datafile_id)
		if data is None:
			py_ubi_forge.log.warn(__name__, f"Failed to find file {file_id:016X}")
			return
		model_name = data.file_name

		obj_handler = mesh.Collada(py_ubi_forge, model_name, save_folder)
		obj_handler.export(file_id, forge_file_name, datafile_id)
		obj_handler.save_and_close()
		py_ubi_forge.log.info(__name__, f'Exported {file_id:016X}')
