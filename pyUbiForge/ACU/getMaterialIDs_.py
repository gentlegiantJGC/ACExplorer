from pyUbiForge.misc import Material
import logging
import pyUbiForge


def get_material_ids(file_id: int) -> Material:
	data = pyUbiForge.temp_files(file_id)
	if data is None:
		logging.warning(f"Failed to find file {file_id:016X}")
		return Material(f'{file_id:016X}', missing_no=True)

	name = data.file_name
	material_set_id = pyUbiForge.read_file(data.file).material_set

	data = pyUbiForge.temp_files(material_set_id)
	if data is None:
		logging.warning(f"Failed to find file {material_set_id:016X}")
		return Material(name, missing_no=True)

	material = pyUbiForge.read_file(data.file)
	material.name = name
	return material
