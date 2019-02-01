from pyUbiForge.misc import mesh

plugin_name = 'Export OBJ'
plugin_level = 4
file_type = '415D9568'


def plugin(py_ubi_forge, file_id, forge_file_name, datafile_id, options):
	# TODO add select directory option
	save_folder = py_ubi_forge.CONFIG['dumpFolder']

	data = py_ubi_forge.temp_files(file_id, forge_file_name, datafile_id)
	if data is None:
		py_ubi_forge.log.warn(__name__, f"Failed to find file {file_id:016X}")
		return
	model_name = data['fileName']

	model = py_ubi_forge.read_file(data["rawFile"])
	if model is not None:
		obj_handler = mesh.ObjMtl(py_ubi_forge, model_name, save_folder)
		obj_handler.export(model, model_name)
		obj_handler.save_and_close()
		py_ubi_forge.log.info(__name__, f'Exported {file_id:016X}')
	else:
		py_ubi_forge.log.warn(__name__, f'Failed to export {file_id:016X}')
