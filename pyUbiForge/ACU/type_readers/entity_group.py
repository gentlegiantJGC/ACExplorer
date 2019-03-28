from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
import numpy


class Reader(BaseReader):
	file_type = '3F742D26'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		# cheap method
		# read top transformation matrix
		# jump to next 29 8D 65 EC while in file
		# jump to next 3B 96 6E 53
		# read 3B 96 6E 53
		check_byte_1 = file_object_data_wrapper.read_uint_8()
		if check_byte_1 == 0:
			py_ubi_forge.log.warn(__name__, 'checkbyte is not 3')
			raise Exception
		self.transformation_matrix = file_object_data_wrapper.read_numpy(numpy.float32, 64, out_file, indent_count).reshape((4, 4))
		file_object_data_wrapper.out_file_write('\n', out_file, indent_count)

		self.file_id_list = []

		"""
		filePointer = fIn.tell()
		rawFile = fIn.read()
		visualLoc = rawFile.find('\x29\x8D\x65\xEC')

		while visualLoc != -1:
			fIn.seek(filePointer)
			readStr(fIn, fOut, visualLoc - 8)

			# jump to mesh
			filePointer = fIn.tell()
			rawFile = fIn.read()
			bbloc = rawFile.find('\x3B\x96\x6E\x53')
			if bbloc == -1:
				return fileContainer
			fIn.seek(filePointer)
			readStr(fIn, fOut, bbloc - 8)

			subFileContainer = py_ubi_forge.read_file.get_data_recursive(file_object_data_wrapper, out_file, indent_count)
			if subFileContainer['meshID'] not in fileContainer['fileIDList']:
				fileContainer['fileIDList'][subFileContainer['meshID']] = []
			if len(subFileContainer['tm']) != len(subFileContainer['BB']):
				raise Exception('should these be the same size?')
			for a in range(len(subFileContainer['tm'])):
				fileContainer['fileIDList'][subFileContainer['meshID']].append(
					{
						'tm': [fileContainer['transformationMtx']] + [subFileContainer['tm'][a]],
						'BB': subFileContainer['BB']
					}
				)
			if len(subFileContainer['tm']) == 0:
				fileContainer['fileIDList'][subFileContainer['meshID']].append(
					{
						'tm': [fileContainer['transformationMtx']]
					}
				)

			filePointer = fIn.tell()
			rawFile = fIn.read()
			visualLoc = rawFile.find('\x29\x8D\x65\xEC')

		fIn.seek(filePointer)
		"""

		# checkByte1 = readInt(fIn, fOut, 1)
		# if checkByte1 == 0:
		# file_object_data_wrapper.read_id(out_file, indent_count)
		# fileType2 = readType(fIn, fOut)
		# recursiveFormat(py_ubi_forge, fileType2, fIn, fOut)
		# file_object_data_wrapper.read_id(out_file, indent_count)
		# fileType2 = readType(fIn, fOut)
		# recursiveFormat(py_ubi_forge, fileType2, fIn, fOut)
		# fileContainer['transformationMtx'] = [[],[],[],[]]
		# for _ in range(4):
		# for m in range(4):
		# fileContainer['transformationMtx'][m].append(file_object_data_wrapper.read_float_32(out_file, indent_count))
		# file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		# count1 = file_object_data_wrapper.read_uint_32(out_file, indent_count)
		# for _ in range(count1):
		# file_object_data_wrapper.read_bytes(2, out_file, indent_count)
		# file_object_data_wrapper.read_id(out_file, indent_count)
		# fileType2 = readType(fIn, fOut)
		# recursiveFormat(py_ubi_forge, fileType2, fIn, fOut)

		# readStr(fIn, fOut, 43)

		# for _ in range(3):
		# file_object_data_wrapper.read_id(out_file, indent_count)
		# fileType2 = readType(fIn, fOut)
		# recursiveFormat(py_ubi_forge, fileType2, fIn, fOut)
		# file_object_data_wrapper.out_file_write('\n', out_file, indent_count)
		# return fileContainer
