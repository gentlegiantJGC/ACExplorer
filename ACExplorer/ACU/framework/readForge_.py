import os


def read_forge(app, folder):
	file_list = {}
	app.file_tree.insert('', 'end', app.gameFunctions.gameIdentifier, text=app.gameFunctions.gameIdentifier)
	for forge_file_name in os.listdir(folder):
		if forge_file_name.endswith('.forge'):
			app.log.info(__name__, 'Building file tree for {}'.format(forge_file_name))
			forge_file = app.misc.file_object.FileObjectDataWrapper.from_file(app, os.path.join(folder, forge_file_name))
			# header
			if forge_file.read_str(8) != b'scimitar':
				continue
			app.file_tree.insert(app.gameFunctions.gameIdentifier, 'end', '{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name), text=forge_file_name)
			file_list[forge_file_name] = {}
			forge_file.seek(1, 1)
			forge_file_version, file_data_header_offset = forge_file.read_struct('iQ')
			if forge_file_version != 27:
				raise Exception('Unsupported Forge file format : "{}"'.format(forge_file_version))
			forge_file.seek(file_data_header_offset+36)
			file_data_offset = forge_file.read_int_64()
			forge_file.seek(file_data_offset)
			# File Data
			index_count, index_table_offset, file_data_offset2, name_table_offset, raw_data_table_offset = forge_file.read_struct('i4x2q8x2q')
			forge_file.seek(index_table_offset)
			index_table = forge_file.read_struct('QQI'*index_count)
			forge_file.seek(name_table_offset)
			name_table = forge_file.read_struct('i40x128s20x'*index_count)
			forge_datafiles = {}
			for n in range(index_count):
				file_id = index_table[n*3+1]
				file_name = name_table[n*2+1].replace(b'\x00', b'').decode("utf-8")
				if index_table[n*3+2] != name_table[n*2]:
					raise Exception('These should be the same. Is something wrong?')
				file_list[forge_file_name][file_id] = {  # file data id (matches the id in the file)
					'rawDataOffset': index_table[n*3],
					'rawDataSize': index_table[n*3+2],
					'fileName': file_name
				}

				if file_name not in forge_datafiles:
					forge_datafiles[file_name] = []
				forge_datafiles[file_name].append(file_id)

			for file_name in sorted(forge_datafiles, key=lambda v: v.lower()):
				for file_id in forge_datafiles[file_name]:
					app.file_tree.insert('{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name), 'end', '{}|{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name, file_id), text=file_name)
			forge_file.close()
	return file_list
