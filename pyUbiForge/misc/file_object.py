import os
import struct
import numpy


class FileObject:
	def __init__(self, path=None, mode='w', data=''):
		self.path = None
		self.mode = None
		self._data = data
		if path is not None:
			if 'r' in mode:
				with open(path, mode) as f:
					self._data = f.read()
			else:
				self._data = ''
				self.path = path
				self.mode = mode
		self._file_pointer = 0

	def tell(self):
		return self._file_pointer

	def write(self, s):
		self._data += s
		self._file_pointer += len(s)

	def read(self, length='end'):
		if length == 'end':
			data = self._data[self._file_pointer:]
			self._file_pointer = len(self._data)
			return data
		else:
			try:
				length = int(length)
				data = self._data[self._file_pointer:self._file_pointer + length]
				self._file_pointer += length
				return data
			except ValueError:
				raise Exception(f'Unsupported type: "{type(length)}"')

	def seek(self, offset, whence=0):
		if whence == 0:
			self._file_pointer = offset
		elif whence == 1:
			self._file_pointer += offset
		elif whence == 2:
			self._file_pointer = len(self._data) - offset

	def close(self, path=None, mode=None):
		if path is not None:
			self.path = path
		if mode is not None:
			self.mode = mode
		if self.mode in 'wa' and self.path is not None and self.mode is not None:
			if not os.path.isdir(os.path.dirname(self.path)):
				os.makedirs(os.path.dirname(self.path))
			with open(self.path, self.mode) as f:
				f.write(self._data)


class FileObjectDataWrapper:
	def __init__(self, py_ubi_forge, file_object, endianness='<'):
		self.pyUbiForge = py_ubi_forge
		self.file_object = file_object
		self.endianness = endianness
		self.indent_chr = '\t'

	@classmethod
	def from_binary(cls, py_ubi_forge, binary, endianness='<'):
		return cls(py_ubi_forge, FileObject(data=binary, mode='r'), endianness)

	@classmethod
	def from_file(cls, py_ubi_forge, path, endianness='<'):
		return cls(py_ubi_forge, open(path, 'rb'), endianness)

	def close(self):
		self.file_object.close()

	def seek(self, offset, whence=0, out_file=None, indent_count=0):
		if out_file is None:
			self.file_object.seek(offset, whence)
		else:
			if whence == 0:  # absolute
				count = offset - self.file_object.tell()
				if count > 0:
					out_file.write(f'{indent_count * self.indent_chr}{hex_string(self.file_object.read(count))}\n')
				elif count < 0:
					out_file.write(f'Skipped back {abs(count)} bytes\n')
					self.file_object.seek(offset, whence)
			elif whence == 1:  # relative
				if offset > 0:
					out_file.write(f'{indent_count * self.indent_chr}{hex_string(self.file_object.read(offset))}\n')
				elif offset < 0:
					out_file.write(f'Skipped back {abs(offset)} bytes\n')
					self.file_object.seek(offset, whence)
			elif whence == 2:  # relative to end
				file_pointer = self.file_object.tell()
				self.file_object.seek(offset, 2)
				count = self.file_object.tell() - file_pointer
				self.file_object.seek(file_pointer)
				if count > 0:
					out_file.write(f'{indent_count * self.indent_chr}{hex_string(self.file_object.read(count))}\n')
				elif count < 0:
					out_file.write(f'Skipped back {abs(count)} bytes\n')
					self.file_object.seek(offset, whence)

	def out_file_write(self, val, out_file=None, indent_count=0):
		if out_file is not None:
			out_file.write(f'{indent_count * self.indent_chr}{val}')

	def _read_struct(self, out_file, indent_count, data_type, trailing_newline=True):
		fmt = f'{self.endianness}{data_type}'
		num_len = struct.calcsize(fmt)
		binary = self.file_object.read(num_len)
		if len(binary) != num_len:
			raise Exception('Reached End Of File')
		val = struct.unpack(data_type, binary)[0]
		if out_file is not None:
			if type(val) == bytes and len(val) > 10:
				out_file.write(
					f'{indent_count * self.indent_chr}{hex_string(binary)}'
				)
			else:
				out_file.write(
					f'{indent_count * self.indent_chr}{hex_string(binary)}\t{val}'
				)

			if trailing_newline:
				out_file.write('\n')
		return val

	def read_bool(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, '?')

	def read_int_8(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'b')

	def read_uint_8(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'B')

	def read_int_16(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'h')

	def read_uint_16(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'H')

	def read_int_32(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'i')

	def read_uint_32(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'I')

	def read_float_32(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'f')

	def read_int_64(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'q')

	def read_uint_64(self, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, 'Q')

	def read_str(self, chr_len, out_file=None, indent_count=0):
		return self._read_struct(out_file, indent_count, f'{chr_len}s')

	def read_id(self, out_file=None, indent_count=0):
		file_id = self._read_struct(out_file, indent_count, self.pyUbiForge.game_functions.file_id_datatype, False)
		if out_file is not None:
			data = self.pyUbiForge.temp_files(file_id)
			if data is None:
				out_file.write('\tUnknown File ID\n')
			else:
				out_file.write('\t{data[fileName]}\t{data[fileType]}\n'.format(data=data))
		return file_id

	def read_type(self, out_file=None, indent_count=0):
		binary = self.file_object.read(self.pyUbiForge.game_functions.file_type_length)
		if len(binary) != self.pyUbiForge.game_functions.file_type_length:
			raise Exception('Reached End Of File')
		file_type = ''.join(f'{b:02X}' for b in binary[::-1])
		if out_file is not None:
			out_file.write(f'{indent_count * self.indent_chr}{hex_string(binary)}\t{file_type}\t{self.pyUbiForge.game_functions.file_types.get(file_type, "Undefined")}\n')
		return file_type

	def read_struct(self, data_types, out_file=None, indent_count=0):
		fmt = f'{self.endianness}{data_types}'
		binary = self.file_object.read(struct.calcsize(fmt))
		if len(binary) != struct.calcsize(fmt):
			raise Exception('Reached End Of File')
		val = struct.unpack(fmt, binary)
		if out_file is not None:
			out_file.write(f'{indent_count * self.indent_chr}{hex_string(binary)}\t{val}\n')
		return val

	def read_numpy(self, dtype, binary_size, out_file=None, indent_count=0):
		binary = self.file_object.read(binary_size)
		if len(binary) != binary_size:
			raise Exception('Reached End Of File')
		val = numpy.fromstring(binary, dtype)
		if out_file is not None:
			out_file.write(f'{indent_count * self.indent_chr}{hex_string(binary)}\t{val}\n')
		return val

	def read_rest(self, out_file=None, indent_count=0):
		binary = self.file_object.read()
		if out_file is not None:
			out_file.write(f'{indent_count * self.indent_chr}{hex_string(binary)}\n')
		return binary

	def clever_format(self, out_file=None, indent_count=0):
		if out_file is not None:
			hex_str = []
			might_be_a_file_type = ''.join(f'{b:02X}' for b in self.file_object.read(4)[::-1])
			while len(might_be_a_file_type) == 8:
				if might_be_a_file_type in self.pyUbiForge.game_functions.file_types:
					out_file.write(f'{indent_count * self.indent_chr}{" ".join(hex_str)}\n')
					out_file.write(f'{indent_count * self.indent_chr}{might_be_a_file_type}\t{self.pyUbiForge.game_functions.file_types.get(might_be_a_file_type)}\n')
					hex_str = []
					might_be_a_file_type = ''.join(f'{b:02X}' for b in self.file_object.read(4)[::-1])
				else:
					hex_str.append(might_be_a_file_type[6:])
					might_be_a_file_type = '{:02X}'.format(ord(self.file_object.read(1))) + might_be_a_file_type[:6]
			while might_be_a_file_type != '':
				hex_str.append(might_be_a_file_type[-2:])
				might_be_a_file_type = might_be_a_file_type[:-2]
			out_file.write(f'{indent_count * self.indent_chr}{" ".join(hex_str)}\n')
		return


def hex_string(binary):
	return ' '.join(f'{b:02X}' for b in binary)
