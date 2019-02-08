import struct
import binascii
import json
import re
from pyUbiForge.misc.plugins import BasePlugin


class Plugin(BasePlugin):
	plugin_name = 'Generate Full Hierarchy'
	plugin_level = 1
	dev = True

	"""This requires temp files to be fully populated so decompress everything first if it isn't already"""

	"""
	{
		file_id : [
			file_name
			file_type,
			[
				[
					forge_file_name,
					datafile_id,
					datafile_name
					[contained_file_ids]
				]
			],
			[files_ids_that_reference]
		]
	}
	"""

	def run(self, py_ubi_forge, *_):
		dict_doc = {}
		file_list = set([binascii.hexlify(struct.pack('<Q', file_id)).decode("utf-8").upper() for file_id in py_ubi_forge.temp_files.list_light_dictionary])
		datafile_count = 0
		datafile_completed_count = 0
		for forge_file_name in py_ubi_forge.forge_files:
			datafile_count += len(py_ubi_forge.forge_files[forge_file_name].datafiles)

		for forge_file_name, forge_file_class in py_ubi_forge.forge_files.items():
			for datafile_id, datafile_class in forge_file_class.datafiles.items():
				datafile_id_hex = binascii.hexlify(struct.pack('<Q', datafile_id)).decode("utf-8").upper()
				try:
					py_ubi_forge.temp_files(datafile_id, forge_file_name, datafile_id)
				except:
					continue
				for file_id in datafile_class.files.keys():
					file_id_hex = binascii.hexlify(struct.pack('<Q', file_id)).decode("utf-8").upper()
					temp_file = py_ubi_forge.temp_files(file_id, forge_file_name, datafile_id)
					file_wrapper = temp_file.file
					file_wrapper.seek(9)
					file_type = file_wrapper.read_type()
					if file_id_hex not in dict_doc:
						dict_doc[file_id_hex] = [temp_file.file_name, file_type, [], []]
					elif dict_doc[file_id_hex][0] is None:
						dict_doc[file_id_hex][0] = temp_file.file_name
						dict_doc[file_id_hex][1] = file_type
					dict_doc[file_id_hex][2].append([forge_file_name, datafile_id_hex, []])
					for potential_file_id in re.findall(b'(?=(.{4}[^\x00]\x00{3}))', file_wrapper.read_rest(), flags=re.DOTALL):
						potential_file_id_hex = binascii.hexlify(potential_file_id).decode("utf-8").upper()
						if potential_file_id_hex in file_list:
							# we have found a valid file reference
							if potential_file_id_hex not in dict_doc[file_id_hex][2][-1][2]:
								dict_doc[file_id_hex][2][-1][2].append(potential_file_id_hex)

							if potential_file_id_hex not in dict_doc:
								dict_doc[potential_file_id_hex] = [None, None, [], []]
							if file_id_hex not in dict_doc[potential_file_id_hex][3]:
								dict_doc[potential_file_id_hex][3].append(file_id_hex)
				datafile_completed_count += 1
				py_ubi_forge.log.info(__name__, f"Processed {round(100*datafile_completed_count/datafile_count, 2)}% of {datafile_count} datafiles")
		py_ubi_forge.log.info(__name__, "Processed all files")
		with open(f'{py_ubi_forge.CONFIG["dumpFolder"]}/ACU_hierarchy.json', 'w') as f:
			json.dump(dict_doc, f, indent=4)
