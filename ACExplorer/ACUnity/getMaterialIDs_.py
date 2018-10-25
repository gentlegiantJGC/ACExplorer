from ACExplorer.misc.dataTypes import uint64


def getMaterialIDs(app, file_id):
	data = app.tempNewFiles.getData(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {}".format(file_id))
		return Material('{:08x}'.format(file_id).upper(), missing_no=True)
	name = data["fileName"]
	material_file = app.misc.FileObject()
	material_file.write(data["rawFile"])
	material_file.seek(26)
	material_template_id = uint64(material_file)

	data = app.tempNewFiles.getData(material_template_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {}".format('{:08x}'.format(material_template_id).upper()))
		return Material(name, missing_no=True)
	materialTemplate = app.misc.FileObject()
	materialTemplate.write(data["rawFile"])
	materialTemplate.seek(0)

	material = Material(name)
	materialTemplate.seek(16, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		material.diffuse = idtemp

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		material.normal = idtemp

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		material.specular = idtemp

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		material.height = idtemp

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		raise Exception('{} has an id in position 5'.format(data['dir']))

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		material.transmission = idtemp

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		raise Exception('{} has an id in position 7'.format(data['dir']))

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		material.mask1 = idtemp

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		material.mask2 = idtemp

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		raise Exception('{} has an id in position 10'.format(data['dir']))

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		raise Exception('{} has an id in position 11'.format(data['dir']))

	materialTemplate.seek(2, 1)
	idtemp = uint64(materialTemplate)
	if idtemp != 0:
		raise Exception('{} has an id in position 12'.format(data['dir']))
	
	return material

class Material:
	def __init__(self, name, missing_no=False, diffuse=None, normal=None, specular=None, height=None, transmission=None, mask1=None, mask2=None):
		self.name = name
		self.missing_no = missing_no
		self.diffuse = diffuse
		self.normal = normal
		self.specular = specular
		self.height = height
		self.transmission = transmission
		self.mask1 = mask1
		self.mask2 = mask2
