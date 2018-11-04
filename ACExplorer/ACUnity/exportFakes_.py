import numpy
# from ACExplorer.misc.dataTypes import uint64


def export_fakes(app, file_id):
	data = app.tempNewFiles.getData(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return
	model_name = data['fileName']
	files = data['rawFile'].split(b'\x00\x00\x00\x00\x00\x00\x00\x00\x24\xB5\x7F\xD7')[1:]
	obj_handler = app.misc.mesh.ObjMtl(app, model_name)
	for n in files:
		if b'\x29\x8D\x65\xEC' not in n:
			continue
		transformation_matrix = numpy.fromstring(n[15:79], numpy.float32).reshape(4, 4)
		visualLoc = n.find(b'\x29\x8D\x65\xEC')
		model_file_id = uint64(n[visualLoc + 8:visualLoc + 16])
		model = app.gameFunctions.read_model(app, model_file_id)
		if model is not None:
			model.vertices = numpy.matmul(numpy.pad(model.vertices, ((0, 0), (0, 1)), 'constant', constant_values=1), transformation_matrix)[:,:3]
			obj_handler.export(model)
	obj_handler.save_and_close()
	app.log.info(__name__, 'Exported {:016X}'.format(file_id))
