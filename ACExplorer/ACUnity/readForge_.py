import os
import struct

def read_forge(app, folder):
	file_list = {}
	for forge_file_name in os.listdir(folder):
		if forge_file_name.endswith('.forge'):
			app.log.info(__name__, 'Building file tree for {}'.format(forge_file_name))
			forge_file = open(os.path.join(folder, forge_file_name), 'rb')
			# header
			if forge_file.read(8) != 'scimitar':
				continue
			app.fileTree.insert(app.gameFunctions.gameIdentifier, 'end', '{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name), text=forge_file_name)
			file_list[forge_file_name] = {}
			forge_file.seek(1, 1)
			forge_file_version, file_data_header_offset = struct.unpack('<iQ', forge_file.read(12))
			if forge_file_version != 27:
				raise Exception('Unsupported Forge file format : "{}"'.format(forge_file_version))
			forge_file.seek(file_data_header_offset+36)
			file_data_offset = struct.unpack('<q', forge_file.read(8))[0]
			forge_file.seek(file_data_offset)
			# File Data
			index_count, index_table_offset, file_data_offset2, name_table_offset, raw_data_table_offset = struct.unpack('<i4x2q8x2q', forge_file.read(48))
			forge_file.seek(index_table_offset)
			index_table = struct.unpack('<'+'QQI'*index_count, forge_file.read(20*index_count))
			forge_file.seek(name_table_offset)
			name_table = struct.unpack('<'+'i40x128s20x'*index_count, forge_file.read(192*index_count))
			forge_datafiles = {}
			for n in xrange(index_count):
				file_id = index_table[n*3+1]
				file_name = name_table[n*2+1].replace('\x00', '')
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
					app.fileTree.insert('{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name), 'end', '{}|{}|{}'.format(app.gameFunctions.gameIdentifier, forge_file_name, file_id), text=file_name)
			forge_file.close()
	return file_list
