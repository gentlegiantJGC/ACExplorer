from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader


class Reader(BaseReader):
	file_type = 'EC658D29'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		file_object_data_wrapper.read_bytes(4, out_file, indent_count)
		file_object_data_wrapper.read_id(out_file, indent_count)

		ending0 = file_object_data_wrapper.read_bytes(1, out_file, indent_count)

		# this totally isn't the correct way to read this but I
		# can't work out how many sub-files should be read and
		# this is the only way I can work out how to do it.
		# while ending0 == '00':
		# file_object_data_wrapper.read_id(out_file, indent_count) # temporary id?
		# fileType2 = readType(fIn, fOut)
		# recursiveFormat(py_ubi_forge, fileType2, fIn, fOut)
		# ending0 = file_object_data_wrapper.read_bytes(1, out_file, indent_count)
		# while ending0 == '03':
		# ending0 = file_object_data_wrapper.read_bytes(1, out_file, indent_count)
		py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
		file_object_data_wrapper.read_bytes(1, out_file, indent_count)

		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)

		for _ in range(7):
			file_object_data_wrapper.read_float_32(out_file, indent_count)
