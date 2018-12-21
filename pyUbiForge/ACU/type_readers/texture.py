import os
import struct
from pyUbiForge.misc import BaseTexture

file_type = 'A2B7E917'


def plugin(py_ubi_forge, file_object_data_wrapper, out_file, indent_count):
	return Texture(py_ubi_forge, file_object_data_wrapper, out_file, indent_count)


class Texture(BaseTexture):
	def __init__(self, py_ubi_forge, texture_file, out_file, indent_count):
		BaseTexture.__init__(self, py_ubi_forge)
		if py_ubi_forge.dev:
			with open(os.path.join(py_ubi_forge.CONFIG['dumpFolder'], 'fileTypes', 'A2B7E917'), 'a') as f2:
				f2.write('{}\n'.format(' '.join(f'{b:02X}' for b in texture_file.read_str(116))))
				texture_file.seek(-116, 1)
		# header has already been read

		self.dwSize = b'\x7C\x00\x00\x00'  # 124
		DDSD_CAPS = DDSD_HEIGHT = DDSD_WIDTH = DDSD_PIXELFORMAT = True
		# (probably should be set based on the data)
		DDSD_PITCH = False
		DDSD_MIPMAPCOUNT = True
		DDSD_LINEARSIZE = True
		DDSD_DEPTH = False
		self.dwFlags = struct.pack('<i', (0x1*DDSD_CAPS)|(0x2*DDSD_HEIGHT)|(0x4*DDSD_WIDTH)|(0x8*DDSD_PITCH)|(0x1000*DDSD_PIXELFORMAT)|(0x20000*DDSD_MIPMAPCOUNT)|(0x80000*DDSD_LINEARSIZE)|(0x800000*DDSD_DEPTH))
		self.dwWidth = texture_file.read_str(4, out_file, indent_count)
		self.dwHeight = texture_file.read_str(4, out_file, indent_count)
		self.dwDepth = texture_file.read_str(4, out_file, indent_count)
		self.imgDXT = texture_file.read_uint_32()
		texture_file.seek(8, 1, out_file, indent_count)  # could be image format. Volume textures have first 4 \x03\x00\x00\x00 all else have \x01\x00\x00\x00
		# next 4 are \x01\x00\x00\x00 for diffuse maps and \x00\x00\x00\x00 for other things like volume textures and maps
		self.dwMipMapCount = texture_file.read_str(4, out_file, indent_count)
		texture_file.seek(84, 1, out_file, indent_count)  # 24 of other data followed by "CompiledTextureMap" which duplicates most of the data
		self.dwPitchOrLinearSize = texture_file.read_str(4, out_file, indent_count)
		self.buffer = texture_file.read_str(struct.unpack('<I', self.dwPitchOrLinearSize)[0], out_file, indent_count)
		self.dwReserved = b'\x00\x00\x00\x00'*11

		self.ddspf = b''  # (pixel format)
		self.ddspf += b'\x20\x00\x00\x00'  # dwSize
		if self.imgDXT in [0, 7]:  # dwFlags
			self.ddspf += b'\x40\x00\x00\x00'
		else:
			self.ddspf += b'\x04\x00\x00\x00'
		# if imgDXT in [0, 7]:
		# 	self.ddspf += b'DXT1'
		if self.imgDXT in [0, 1, 2, 3, 7]:  # dwFourCC
			self.ddspf += b'DXT1'
		elif self.imgDXT == 4:
			self.ddspf += b'DXT3'
		elif self.imgDXT in [5, 6]:
			self.ddspf += b'DXT5'
		elif self.imgDXT in [8, 9, 16]:
			self.ddspf += b'DX10'
		else:
			raise Exception(f'imgDXT: "{self.imgDXT}" is not currently supported')

		self.ddspf += b'\x00\x00\x00\x00' * 5  # dwRGBBitCount, dwRBitMask, dwGBitMask, dwBBitMask, dwABitMask
		if self.imgDXT == 8:
			self.DXT10Header = b'\x62\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
		else:
			self.DXT10Header = b''
		self.dwCaps = b'\x08\x10\x40\x00'
		self.dwCaps2 = b'\x00\x00\x00\x00'
		self.dwCaps3 = b'\x00\x00\x00\x00'
		self.dwCaps4 = b'\x00\x00\x00\x00'
		self.dwReserved2 = b'\x00\x00\x00\x00'
