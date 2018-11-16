import os


def read_compressed_data_section(app, raw_data_chunk):
	raw_data_chunk.seek(2, 1)
	compression_type = raw_data_chunk.read_uint_8()
	raw_data_chunk.seek(3, 1)
	format_version = raw_data_chunk.read_uint_8()
	if format_version == 0:
		uncompressed_data_list = []
		comp_block_count = 1
		while comp_block_count == 1:
			try:
				comp_block_count = raw_data_chunk.read_uint_8()
			except:
				comp_block_count = 0
				continue
			if comp_block_count != 1:
				raise Exception('This file has a count not equal to 1. No example of this has been found yet. Please let the creator know where you found this.')
			size_table = raw_data_chunk.read_numpy('<u4', comp_block_count * 8).reshape(-1, 2).astype(int)  # 'compressed_size', 'uncompressed_size'
			for size in size_table:  # Could do this using numpy and then vectorise the decompression
				raw_data_chunk.seek(4, 1)  # I think this is the hash of the data
				uncompressed_data_list.append(app.misc.decompress(compression_type, raw_data_chunk.read_str(size[0]), size[1]))

	elif format_version == 128:
		comp_block_count = raw_data_chunk.read_uint_32()
		size_table = raw_data_chunk.read_numpy('<u2', comp_block_count * 4).reshape(-1, 2).astype(int)  # 'uncompressed_size', 'compressed_size'
		uncompressed_data_list = []
		for size in size_table:  # Could do this using numpy and then vectorise the decompression
			raw_data_chunk.seek(4, 1)  # I think this is the hash of the data
			uncompressed_data_list.append(app.misc.decompress(compression_type, raw_data_chunk.read_str(size[1]), size[0]))
	else:
		raise Exception('Format version not known. Please let the creator know where you found this.')

	return format_version, uncompressed_data_list


def decompress_datafile(app, datafile_id, forge_file_name=None):
	if datafile_id == 0 or datafile_id > 2**40:
		return
	uncompressed_data_list = []

	forge_file = open(os.path.join(app.CONFIG.game_folder(app.gameFunctions.gameIdentifier), forge_file_name), 'rb')
	forge_file.seek(app.file_list[forge_file_name][datafile_id]['rawDataOffset'])
	raw_data_chunk = app.misc.file_object.FileObjectDataWrapper.from_binary(app, forge_file.read(app.file_list[forge_file_name][datafile_id]['rawDataSize']))
	forge_file.close()
	header = raw_data_chunk.read_str(8)
	format_version = 128
	if header == b'\x33\xAA\xFB\x57\x99\xFA\x04\x10':  # if compressed
		format_version, uncompressed_data_list = read_compressed_data_section(app, raw_data_chunk)
		if format_version == 128:
			if raw_data_chunk.read_str(8) == b'\x33\xAA\xFB\x57\x99\xFA\x04\x10':
				_, uncompressed_data_list_ = read_compressed_data_section(app, raw_data_chunk)
				uncompressed_data_list += uncompressed_data_list_
			else:
				raise Exception('Compression Issue. Second compression block not found')
		if len(raw_data_chunk.read_rest()) != 0:
			raise Exception('Compression Issue. More data found')
	else:
		raw_data_chunk_rest = header + raw_data_chunk.read_rest()
		if b'\x33\xAA\xFB\x57\x99\xFA\x04\x10' in raw_data_chunk_rest:
			raise Exception('Compression Issue')
		else:
			uncompressed_data_list.append(raw_data_chunk_rest)  # The file is not compressed

	if format_version == 0:
		alphabetical_files = {}
		app.tempNewFiles.add(datafile_id, forge_file_name, datafile_id, 0, app.file_list[forge_file_name][datafile_id]['fileName'], raw_file=b''.join(uncompressed_data_list))
		alphabetical_files[app.file_list[forge_file_name][datafile_id]['fileName']] = [datafile_id]

	elif format_version == 128:
		uncompressed_data = app.misc.file_object.FileObjectDataWrapper.from_binary(app, b''.join(uncompressed_data_list))

		file_count = uncompressed_data.read_uint_16()
		index_table = []
		alphabetical_files = {}
		for _ in range(file_count):
			index_table.append(uncompressed_data.read_struct('QIH'))  # file_id, data_size (file_size + header), extra16_count (for next line)
			uncompressed_data.seek(index_table[-1][2]*2, 1)
		for index in range(file_count):
			file_type, file_size, file_name_size = uncompressed_data.read_struct('3I')
			file_id = index_table[index][0]
			file_name = uncompressed_data.read_str(file_name_size).decode("utf-8")
			check_byte = uncompressed_data.read_uint_8()
			if check_byte == 1:
				uncompressed_data.seek(3, 1)
				unk_count = uncompressed_data.read_uint_32()
				uncompressed_data.seek(12 * unk_count, 1)
			elif check_byte != 0:
				raise Exception('Either something has gone wrong or a new value has been found here')

			raw_file = uncompressed_data.read_str(file_size)

			if file_name == '':
				file_name = f'{file_id:016X}'
			app.tempNewFiles.add(file_id, forge_file_name, datafile_id, file_type, file_name, raw_file=raw_file)
			if file_name not in alphabetical_files:
				alphabetical_files[file_name] = []
			alphabetical_files[file_name].append(file_id)
			if app.CONFIG['writeToDisk']:
				folder = os.path.join(
					app.CONFIG['dumpFolder'],
					app.gameFunctions.gameIdentifier,
					forge_file_name,
					app.file_list[forge_file_name][datafile_id]['fileName'],
					f'{file_type:08X}'
				)
				if os.path.isfile(os.path.join(folder, f'{file_name}.{app.gameFunctions.gameIdentifier.lower()}')):
					duplicate = 1
					while os.path.isfile(os.path.join(folder, f'{file_name}_{duplicate}.{app.gameFunctions.gameIdentifier.lower()}')):
						duplicate += 1
					path = os.path.join(folder, f'{file_name}_{duplicate}.{app.gameFunctions.gameIdentifier.lower()}')
				else:
					path = os.path.join(folder, f'{file_name}.{app.gameFunctions.gameIdentifier.lower()}')
				if not os.path.isdir(folder):
					os.makedirs(folder)
				try:
					open(path, 'wb').write(raw_file)
				except Exception as e:
					app.log.warn(__name__, f'Error saving temporary file with path "{path}"\n{e}')

	else:
		raise Exception('Format version not known. Please let the creator know where you found this.')
	
	for file_name in sorted(alphabetical_files, key=lambda v: v.lower()):
		for file_id in alphabetical_files[file_name]:
			unique_identifier = f'{app.gameFunctions.gameIdentifier}|{forge_file_name}|{datafile_id}|{file_id}'
			if not app.file_tree.exists(unique_identifier):
				app.file_tree.insert(f'{app.gameFunctions.gameIdentifier}|{forge_file_name}|{datafile_id}', 'end', unique_identifier, text=file_name)
