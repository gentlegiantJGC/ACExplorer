import struct
import numpy
from typing import TextIO, Tuple, Any, TYPE_CHECKING
from io import BytesIO

if TYPE_CHECKING:
	from pyUbiForge2 import BaseGame, BaseFile


NEWLINE = "\n"


class Indent:
	def __enter__(self):
		pass

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass


class FileDataWrapper(BytesIO):
	def __init__(
			self,
			file: bytes,
			game: "BaseGame"
	):
		assert isinstance(file, bytes)
		assert game.endianness in ('<', '>')
		super().__init__(file)
		self._game = game
		self._endianness = game.endianness

	@property
	def indent(self):
		"""with file.indent:"""
		return Indent()

	def out_file_write(self, val: str):
		pass

	def _read_struct(self, data_type: str) -> Tuple[Any]:
		fmt = f'{self._endianness}{data_type}'
		num_len = struct.calcsize(fmt)
		binary = self.read(num_len)
		if len(binary) != num_len:
			raise EOFError('Reached End Of File')
		return struct.unpack(fmt, binary)

	def read_struct(self, data_types: str) -> Tuple[Any]:
		# data_types should not be prefixed with the endianness (this is added on for you)
		return self._read_struct(data_types)

	def read_bool(self) -> bool:
		return self._read_struct('?')[0]

	def read_int_8(self) -> int:
		return self._read_struct('b')[0]

	def read_uint_8(self) -> int:
		return self._read_struct('B')[0]

	def read_int_16(self) -> int:
		return self._read_struct('h')[0]

	def read_uint_16(self) -> int:
		return self._read_struct('H')[0]

	def read_int_32(self) -> int:
		return self._read_struct('i')[0]

	def read_uint_32(self) -> int:
		return self._read_struct('I')[0]

	def read_float_32(self) -> int:
		return self._read_struct('f')[0]

	def read_int_64(self) -> int:
		return self._read_struct('q')[0]

	def read_uint_64(self) -> int:
		return self._read_struct('Q')[0]

	def read_bytes(self, chr_len: int) -> bytes:
		return self._read_struct(f'{chr_len}s')[0]

	def read_file_id(self) -> int:
		return self._read_struct(self._game.FileIDType)[0]

	def read_resource_type(self) -> int:
		return self._read_struct(self._game.ResourceType)[0]

	def read_file(self) -> "BaseFile":
		return self._game.read_file(self)

	def read_numpy(self, dtype, binary_size: int) -> numpy.ndarray:
		binary = self.read(binary_size)
		if len(binary) != binary_size:
			raise EOFError('Reached End Of File')
		return numpy.copy(numpy.frombuffer(binary, dtype))

	def read_rest(self) -> bytes:
		return self.read()

	def clever_format(self):
		pass


class FormatIndent:
	def __init__(self, wrapper: "FileFormatDataWrapper"):
		self._wrapper = wrapper

	def __enter__(self):
		self._wrapper.indent_count += 1

	def __exit__(self, exc_type, exc_val, exc_tb):
		self._wrapper.indent_count -= 1


class FileFormatDataWrapper(FileDataWrapper):
	def __init__(
			self,
			file: bytes,
			game: "BaseGame",
			out_file: TextIO
	):
		super().__init__(file, game)
		self._out_file = out_file
		self.indent_count = 0
		self.indent_chr = '\t'

	@property
	def indent(self):
		return FormatIndent(self)

	def close(self):
		super().close()
		self._out_file.close()

	def seek(self, offset: int, whence: int = 0):
		if whence == 0:  # absolute
			count = offset - self.tell()
			if count > 0:
				self._out_file.write(f'{self.indent_count * self.indent_chr}{hex_string(self.read(count))}\n')
			elif count < 0:
				self._out_file.write(f'Skipped back {abs(count)} bytes\n')
				super().seek(offset, whence)
		elif whence == 1:  # relative
			if offset > 0:
				self._out_file.write(f'{self.indent_count * self.indent_chr}{hex_string(self.read(offset))}\n')
			elif offset < 0:
				self._out_file.write(f'Skipped back {abs(offset)} bytes\n')
				super().seek(offset, whence)
		elif whence == 2:  # relative to end
			file_pointer = self.tell()
			super().seek(offset, 2)
			count = self.tell() - file_pointer
			super().seek(file_pointer)
			if count > 0:
				self._out_file.write(f'{self.indent_count * self.indent_chr}{hex_string(self.read(count))}\n')
			elif count < 0:
				self._out_file.write(f'Skipped back {abs(count)} bytes\n')
				super().seek(offset, whence)

	def out_file_write(self, val: str):
		self._out_file.write(f'{self.indent_count * self.indent_chr}{val}')

	def _read_struct(self, data_type: str, trailing_newline: bool = True) -> Tuple[Any]:
		fmt = f'{self._endianness}{data_type}'
		num_len = struct.calcsize(fmt)
		binary = self.read(num_len)
		if len(binary) != num_len:
			raise EOFError('Reached End Of File')
		val = struct.unpack(fmt, binary)
		self._out_file.write(
			f'{self.indent_count * self.indent_chr}{hex_string(binary)}\t\t{val}{NEWLINE * trailing_newline}'
		)
		return val

	def read_file_id(self) -> int:
		file_id = self._read_struct(self._game.FileIDType, False)[0]
		file_location = self._game.find_file(file_id)
		if file_location is None:
			self._out_file.write('\t\tUnknown File ID\n')
		else:
			forge_file, data_file = file_location
			file_type, file_name = self._game.get_forge_file(forge_file).get_data_file(data_file).get_file(file_id)
			self._out_file.write(f'\t\t{file_name}\t{file_type}\n')
		return file_id

	def read_resource_type(self) -> int:
		file_type = super().read_resource_type()
		self._out_file.write(f'{self.indent_count * self.indent_chr}{file_type:08X}\t\t{file_type}\t{self._game.file_types.get(file_type, "Undefined")}\n')
		return file_type

	def read_numpy(self, dtype, binary_size: int):
		val = super().read_numpy(dtype, binary_size)
		if self._out_file is not None:
			self._out_file.write(f'{self.indent_count * self.indent_chr}\t\t{val}\n')
		return val

	def read_rest(self) -> bytes:
		binary = self.read()
		if self._out_file is not None:
			self._out_file.write(f'{self.indent_count * self.indent_chr}{hex_string(binary)}\n')
		return binary

	# def clever_format(self):
	# 	if self._out_file is not None:
	# 		hex_str = []
	# 		might_be_a_file_type = ''.join(f'{b:02X}' for b in self.read(4)[::-1])
	# 		while len(might_be_a_file_type) == 8:
	# 			if might_be_a_file_type in pyUbiForge.game_functions.file_types:
	# 				self._out_file.write(f'{self._indent_count * self.indent_chr}{" ".join(hex_str)}\n')
	# 				self._out_file.write(f'{self._indent_count * self.indent_chr}{might_be_a_file_type}\t\t{pyUbiForge.game_functions.file_types.get(might_be_a_file_type)}\n')
	# 				hex_str = []
	# 				might_be_a_file_type = ''.join(f'{b:02X}' for b in self.read(4)[::-1])
	# 			else:
	# 				hex_str.append(might_be_a_file_type[6:])
	# 				next_chr = self.read(1)
	# 				if next_chr == b'':
	# 					might_be_a_file_type = might_be_a_file_type[:6]
	# 				else:
	# 					might_be_a_file_type = f'{next_chr[0]:02X}{might_be_a_file_type[:6]}'
	#
	# 		while might_be_a_file_type != '':
	# 			hex_str.append(might_be_a_file_type[-2:])
	# 			might_be_a_file_type = might_be_a_file_type[:-2]
	# 		self._out_file.write(f'{self._indent_count * self.indent_chr}{" ".join(hex_str)}\n')
	# 	return


def hex_string(binary: bytes) -> str:
	return ' '.join(f'{b:02X}' for b in binary)
