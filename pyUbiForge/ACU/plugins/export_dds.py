from pyUbiForge.misc import texture
from pyUbiForge.misc.plugins import BasePlugin
from typing import Union, List


class Plugin(BasePlugin):
	plugin_name = 'Export DDS'
	plugin_level = 4
	file_type = 'A2B7E917'

	def run(self, file_id: Union[str, int], forge_file_name: str, datafile_id: int, options: Union[List[dict], None] = None):
		# TODO add select directory option
		save_folder = py_ubi_forge.CONFIG.get('dumpFolder', 'output')
		texture.export_dds(py_ubi_forge, file_id, save_folder, forge_file_name, datafile_id)
