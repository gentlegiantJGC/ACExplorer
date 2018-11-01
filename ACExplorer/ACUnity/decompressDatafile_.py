import os


def decompress_datafile(app, datafile_id, forge_file_name=None):
	if datafile_id == 0 or datafile_id > 2**40:
		return
	uncompressed_data_list = []

	forge_file = open(os.path.join(app.CONFIG.gameFolder(app.gameFunctions.gameIdentifier), forge_file_name), 'rb')
	forge_file.seek(app.fileList[forge_file_name][datafile_id]['rawDataOffset'])
	raw_data_chunk = app.misc.file_object.FileObjectDataWrapper.from_binary(app, forge_file.read(app.fileList[forge_file_name][datafile_id]['rawDataSize']))
	forge_file.close()
	if raw_data_chunk.read_str(8) == '\x33\xAA\xFB\x57\x99\xFA\x04\x10':  # if compressed
		raw_data_chunk.seek(2, 1)
		compression_type = raw_data_chunk.read_uint_8()
		raw_data_chunk.seek(4, 1)
		comp_block_count = raw_data_chunk.read_uint_32()
		size_table = raw_data_chunk.read_numpy('<u2', comp_block_count * 4).reshape(-1, 2).astype(int)  # 'uncompressed_size', 'compressed_size'
		for size in size_table:
			raw_data_chunk.seek(4, 1)
			uncompressed_data_list.append(app.misc.decompress(compression_type, raw_data_chunk.read_str(size[1]), size[0]))

		if raw_data_chunk.read_str(8) == '\x33\xAA\xFB\x57\x99\xFA\x04\x10':
			raw_data_chunk.seek(2, 1)
			compression_type = raw_data_chunk.read_uint_8()
			raw_data_chunk.seek(4, 1)
			comp_block_count = raw_data_chunk.read_uint_32()
			size_table = raw_data_chunk.read_numpy('<u2', comp_block_count * 4).reshape(-1, 2).astype(int)  # 'uncompressed_size', 'compressed_size'
			for size in size_table:
				raw_data_chunk.seek(4, 1)
				uncompressed_data_list.append(app.misc.decompress(compression_type, raw_data_chunk.read_str(size[1]), size[0]))
		else:
			raise Exception('Compression Issue. Second compression block not found')
		raw_data_chunk_rest = raw_data_chunk.read_rest()
		if '\x33\xAA\xFB\x57\x99\xFA\x04\x10' in raw_data_chunk_rest:
			raise Exception('Compression Issue. More compressed blocks found')
	else:
		raw_data_chunk.seek(0)
		raw_data_chunk_rest = raw_data_chunk.read_rest()
		if '\x33\xAA\xFB\x57\x99\xFA\x04\x10' in raw_data_chunk_rest:
			raise Exception('Compression Issue')
		else:
			uncompressed_data_list.append(raw_data_chunk_rest)  # The file is not compressed

	uncompressed_data = app.misc.file_object.FileObjectDataWrapper.from_binary(app, ''.join(uncompressed_data_list))

	file_count = uncompressed_data.read_uint_16()
	index_table = []
	alphabetical_files = {}
	for _ in range(file_count):
		index_table.append(uncompressed_data.read_struct('QIH'))  # file_id, data_size (file_size + header), extra16_count (for next line)
		uncompressed_data.seek(index_table[-1][2]*2, 1)
	for index in range(file_count):
		file_type, file_size, file_name_size = uncompressed_data.read_struct('3I')
		file_id = index_table[index][0]
		file_name = uncompressed_data.read_str(file_name_size)
		check_byte = uncompressed_data.read_uint_8()
		if check_byte == 1:
			uncompressed_data.seek(3, 1)
			unk_count = uncompressed_data.read_uint_32()
			uncompressed_data.seek(12 * unk_count, 1)
		elif check_byte != 0:
			raise Exception('Either something has gone wrong or a new value has been found here')

		raw_file = uncompressed_data.read_str(file_size)
		uncompressed_data.seek(index_table[index][1] - 13 - file_name_size - file_size, 1)

		if file_name == '':
			file_name = '{:016X}'.format(file_id)
		app.tempNewFiles.add(file_id, forge_file_name, datafile_id, file_type, file_name, rawFile=raw_file)
		if file_name not in alphabetical_files:
			alphabetical_files[file_name] = []
		alphabetical_files[file_name].append(file_id)
		if app.CONFIG['writeToDisk']:
			folder = os.path.join(app.CONFIG['dumpFolder'], app.gameFunctions.gameIdentifier, forge_file_name, app.fileList[forge_file_name][datafile_id]['fileName'], '{:08X}'.format(file_type))
			if os.path.isfile(os.path.join(folder, '{}.{}'.format(file_name, app.gameFunctions.gameIdentifier.lower()))):
				duplicate = 1
				while os.path.isfile(os.path.join(folder, '{}_{}.{}'.format(file_name, duplicate, app.gameFunctions.gameIdentifier.lower()))):
					duplicate += 1
				path = os.path.join(folder, '{}_{}.{}'.format(file_name, duplicate, app.gameFunctions.gameIdentifier.lower()))
			else:
				path = os.path.join(folder, '{}.{}'.format(file_name, app.gameFunctions.gameIdentifier.lower()))
			if not os.path.isdir(folder):
				os.makedirs(folder)
			try:
				open(path, 'wb').write(raw_file)
			except Exception as e:
				app.log.warn(__name__, 'Error saving temporary file with path "{}"\n{}'.format(path, e))
	
	for file_name in sorted(alphabetical_files, key=lambda v: v.lower()):
		for file_id in alphabetical_files[file_name]:
			try:
				app.fileTree.insert('{}|{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name, datafile_id), 'end', '{}|{}|{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name, datafile_id, file_id), text=file_name)
			except:
				continue
