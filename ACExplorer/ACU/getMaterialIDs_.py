def get_material_ids(app, file_id):
	data = app.tempNewFiles(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return app.misc.Material('{:016X}'.format(file_id), missing_no=True)
	name = data["fileName"]

	material_file = data["rawFile"]
	material_file.seek(25)
	material_template_id = material_file.read_id()

	data = app.tempNewFiles(material_template_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(material_template_id))
		return app.misc.Material(name, missing_no=True)
	material_template = data["rawFile"]

	material = app.misc.Material(name)
	material_template.seek(13, 1)

	texture_table = material_template.read_numpy([('', '<u2'), ('texture_id', '<u8')], 120)
	material.diffuse, material.normal, material.specular, \
		material.height, tex5, material.transmission, tex7, \
		material.mask1, material.mask2, tex10, tex11, tex12 \
		= [texture_id if texture_id != 0 else None for texture_id in texture_table['texture_id']]

	for var, pos in [[tex5, 5], [tex7, 7], [tex10, 10], [tex11, 11], [tex12, 12]]:
		if var is not None:
			raise Exception('{} has an id in position {}'.format(data, pos))
	
	return material
