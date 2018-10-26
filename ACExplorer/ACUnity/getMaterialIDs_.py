from ACExplorer.ACUnity.formatFile import readID
import numpy


def getMaterialIDs(app, file_id):
	data = app.tempNewFiles.getData(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return Material('{:016X}'.format(file_id), missing_no=True)
	name = data["fileName"]
	material_file = app.misc.FileObject()
	material_file.write(data["rawFile"])
	material_file.seek(26)
	material_template_id = readID(app, material_file, None)

	data = app.tempNewFiles.getData(material_template_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(material_template_id))
		return Material(name, missing_no=True)
	materialTemplate = app.misc.FileObject()
	materialTemplate.write(data["rawFile"])
	materialTemplate.seek(0)

	material = Material(name)
	materialTemplate.seek(14, 1)

	texture_table = numpy.fromstring(materialTemplate.read(120), dtype=[('', numpy.uint16), ('texture_id', numpy.uint64)])
	material.diffuse, material.normal, material.specular, \
		material.height, tex5, material.transmission, tex7, \
		material.mask1, material.mask2, tex10, tex11, tex12 \
		= [texture_id if texture_id != 0 else None for texture_id in texture_table['texture_id']]

	for var, pos in [[tex5, 5], [tex7, 7], [tex10, 10], [tex11, 11], [tex12, 12]]:
		if var is not None:
			raise Exception('{} has an id in position {}'.format(data, pos))
	
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
