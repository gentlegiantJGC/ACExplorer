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
		elif isinstance(length, int):
			data = self._data[self._file_pointer:self._file_pointer + length]
			self._file_pointer += length
			return data
		else:
			raise Exception('Unsupported type: "{}"'.format(type(length)))

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
	def __init__(self, app, file_object, endianness='<'):
		self.app = app
		self.file_object = file_object
		self.endianness = endianness
		self.indent_chr = '\t'

	@classmethod
	def from_binary(cls, app, binary, endianness='<'):
		return cls(app, FileObject(data=binary, mode='r'), endianness)

	@classmethod
	def from_file(cls, app, path, endianness='<'):
		return cls(app, open(path, 'rb'), endianness)

	def close(self):
		self.file_object.close()

	def seek(self, offset, whence=0, out_file=None, indent_count=0):
		if out_file is None:
			self.file_object.seek(offset, whence)
		else:
			if whence == 0:
				count = offset - self.file_object.tell()
				if count > 0:
					out_file.write('{}{}\n'.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in self.file_object.read(count))))
				elif count < 0:
					out_file.write('Skipped back {} bytes\n'.format(abs(count)))
			elif whence == 1:
				if offset > 0:
					out_file.write('{}{}\n'.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in self.file_object.read(offset))))
				elif offset < 0:
					out_file.write('Skipped back {} bytes\n'.format(abs(offset)))
			elif whence == 2:
				file_pointer = self.file_object.tell()
				self.file_object.seek(offset, 2)
				count = self.file_object.tell() - file_pointer
				self.file_object.seek(file_pointer)
				if count > 0:
					out_file.write('{}{}\n'.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in self.file_object.read(count))))
				elif count < 0:
					out_file.write('Skipped back {} bytes\n'.format(abs(count)))

	@staticmethod
	def out_file_write(self, val, out_file=None, indent_count=0):
		if out_file is not None:
			out_file.write('{}{}'.format(indent_count * self.indent_chr, val))

	def _read_num(self, out_file, indent_count, num_len, data_type, trailing_newline=True):
		binary = self.file_object.read(num_len)
		if len(binary) != num_len:
			raise Exception('Reached End Of File')
		val = struct.unpack('{}{}'.format(self.endianness, data_type), binary)[0]
		if out_file is not None:
			fmt_str = '{}{}\t{}'
			if trailing_newline:
				fmt_str += '\n'
			out_file.write(fmt_str.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in binary), val))
		return val

	def read_int_8(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 1, 'b')

	def read_uint_8(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 1, 'B')

	def read_int_16(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 2, 'h')

	def read_uint_16(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 2, 'H')

	def read_int_32(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 4, 'i')

	def read_uint_32(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 4, 'I')

	def read_float_32(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 4, 'f')

	def read_int_64(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 8, 'q')

	def read_uint_64(self, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, 8, 'Q')

	def read_str(self, chr_len, out_file=None, indent_count=0):
		return self._read_num(out_file, indent_count, chr_len, 's')

	def read_id(self, out_file=None, indent_count=0):
		file_id = self._read_num(out_file, indent_count, 8, 'Q', True)
		if out_file is not None:
			data = self.app.tempNewFiles.getData(file_id)
			out_file.write('\t')
			if data is None:
				out_file.write('Unknown File ID\n')
			else:
				out_file.write('{data[fileName]}\t{data[fileType]}\n'.format(data=data))
		return file_id

	def read_type(self, out_file=None, indent_count=0):
		binary = self.file_object.read(4)
		if len(binary) != 4:
			raise Exception('Reached End Of File')
		file_type = ''.join('{:02X}'.format(ord(b)) for b in binary[::-1])
		if out_file is not None:
			out_file.write('{}{}\t{}\t{}\n'.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in binary), file_type, self.app.gameFunctions.file_types.get(file_type, 'Undefined')))
		return file_type

	def read_struct(self, data_types, out_file=None, indent_count=0):
		fmt = '{}{}'.format(self.endianness, data_types)
		binary = self.file_object.read(struct.calcsize(fmt))
		if len(binary) != struct.calcsize(fmt):
			raise Exception('Reached End Of File')
		val = struct.unpack(fmt, binary)
		if out_file is not None:
			out_file.write('{}{}\t{}\n'.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in binary), val))
		return val

	def read_numpy(self, dtype, binary_size, out_file=None, indent_count=0):
		binary = self.file_object.read(binary_size)
		if len(binary) != binary_size:
			raise Exception('Reached End Of File')
		val = numpy.fromstring(binary, dtype)
		if out_file is not None:
			out_file.write('{}{}\t{}\n'.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in binary), val))
		return val

	def read_rest(self, out_file=None, indent_count=0):
		binary = self.file_object.read()
		if out_file is not None:
			out_file.write('{}{}\n'.format(indent_count * self.indent_chr, ' '.join('{:02X}'.format(ord(b)) for b in binary)))
		return

	def clever_format(self, out_file=None, indent_count=0):
		if out_file is not None:
			hex_str = []
			might_be_a_file_type = ''.join('{:02X}'.format(ord(b)) for b in self.file_object.read(4)[::-1])
			while len(might_be_a_file_type) == 8:
				if might_be_a_file_type in self.app.gameFunctions.file_types:
					out_file.write('{}{}\n'.format(indent_count * self.indent_chr, ' '.join(hex_str)))
					out_file.write('{}{}\t{}\n'.format(indent_count * self.indent_chr, might_be_a_file_type, self.app.gameFunctions.file_types.get(might_be_a_file_type)))
					hex_str = []
					might_be_a_file_type = ''.join('{:02X}'.format(ord(b)) for b in self.file_object.read(4)[::-1])
				else:
					hex_str.append(might_be_a_file_type[6:])
					might_be_a_file_type = '{:02X}'.format(ord(self.file_object.read(1))) + might_be_a_file_type[:6]
			while might_be_a_file_type != '':
				hex_str.append(might_be_a_file_type[-2:])
				might_be_a_file_type = might_be_a_file_type[:-2]
			out_file.write('{}{}\n'.format(indent_count * self.indent_chr, ' '.join(hex_str)))
		return
