from pyUbiForge.misc import texture
from pyUbiForge.misc.plugins import BasePlugin


class Plugin(BasePlugin):
	plugin_name = 'Export DDS'
	plugin_level = 4
	file_type = 'A2B7E917'

	def run(self, py_ubi_forge, file_id, forge_file_name, datafile_id, options):
		# TODO add select directory option
		save_folder = py_ubi_forge.CONFIG['dumpFolder']
		texture.export_dds(py_ubi_forge, file_id, save_folder, forge_file_name, datafile_id)
