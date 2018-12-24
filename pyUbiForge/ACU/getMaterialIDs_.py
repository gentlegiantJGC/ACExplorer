from pyUbiForge.misc import Material


def get_material_ids(py_ubi_forge, file_id):
	data = py_ubi_forge.temp_files(file_id)
	if data is None:
		py_ubi_forge.log.warn(__name__, f"Failed to find file {file_id:016X}")
		return Material(f'{file_id:016X}', missing_no=True)
	name = data["fileName"]

	material_file = data["rawFile"]
	material_file.seek(25)
	material_template_id = material_file.read_id()

	data = py_ubi_forge.temp_files(material_template_id)
	if data is None:
		py_ubi_forge.log.warn(__name__, f"Failed to find file {material_template_id:016X}")
		return Material(name, missing_no=True)
	material_template = data["rawFile"]

	material = Material(name)
	material_template.seek(13, 1)

	texture_table = material_template.read_numpy([('', '<u2'), ('texture_id', '<u8')], 120)
	material.diffuse, material.normal, material.specular, \
		material.height, tex5, material.transmission, tex7, \
		material.mask1, material.mask2, tex10, tex11, tex12 \
		= [texture_id if texture_id != 0 else None for texture_id in texture_table['texture_id']]

	for var, pos in [[tex5, 5], [tex7, 7], [tex10, 10], [tex11, 11], [tex12, 12]]:
		if var is not None:
			raise Exception(f'{data} has an id in position {pos}')
	
	return material
