from pyUbiForge.misc import texture

plugin_name = 'Export DDS'
plugin_level = 4
file_type = 'A2B7E917'


def plugin(py_ubi_forge, file_id, forge_file_name, datafile_id):
	# TODO add select directory option
	save_folder = py_ubi_forge.CONFIG['dumpFolder']
	texture.export_dds(py_ubi_forge, file_id, forge_file_name, datafile_id, save_folder)
