import struct
from pyUbiForge.misc import BaseTexture
from pyUbiForge.misc.file_readers import BaseReader
from pyUbiForge.misc.file_object import FileObjectDataWrapper
#import logging


class Reader(BaseTexture, BaseReader):
	file_type = 'A2B7E917'

	def __init__(self, texture_file: FileObjectDataWrapper):
		BaseTexture.__init__(self)
		self.dwSize = b'\x7C\x00\x00\x00'  # 124
		DDSD_CAPS = DDSD_HEIGHT = DDSD_WIDTH = DDSD_PIXELFORMAT = True
		# (probably should be set based on the data)
		DDSD_PITCH = False
		DDSD_MIPMAPCOUNT = True
		DDSD_LINEARSIZE = True
		DDSD_DEPTH = False
		self.dwFlags = struct.pack('<i', (0x1*DDSD_CAPS)|(0x2*DDSD_HEIGHT)|(0x4*DDSD_WIDTH)|(0x8*DDSD_PITCH)|(0x1000*DDSD_PIXELFORMAT)|(0x20000*DDSD_MIPMAPCOUNT)|(0x80000*DDSD_LINEARSIZE)|(0x800000*DDSD_DEPTH))
		self.dwWidth = texture_file.read_bytes(4)
		self.dwHeight = texture_file.read_bytes(4)
		self.dwDepth = texture_file.read_bytes(4)
		self.imgDXT = texture_file.read_uint_32()
		unk1 = texture_file.read_uint_32() # dimension count. 1 for normal textures, 2 for cube maps and 3 for LUTs
		unk2 = texture_file.read_uint_32()
			# all diffuse maps seem to be 1
			# normal maps: 0
			# specular maps: 1
			# Mask1Map: 0
			# height map: 0
			# transmission map: 1


		#texture_file.seek(8, 1)  # could be image format. Volume textures have first 4 \x03\x00\x00\x00 all else have \x01\x00\x00\x00
		# next 4 are \x01\x00\x00\x00 for diffuse maps and \x00\x00\x00\x00 for other things like volume textures and maps
		self.dwMipMapCount = texture_file.read_bytes(4)

		self.material_type = texture_file.read_uint_32()  # resource type (the same as the index in the texture_set)
			# 0 for diffuse
			# 1 for normal
			# 2 for specular
			# 3 for height
			# 4 ?
			# 5 TransmissionMap
			# 6 ?
			# 7 Mask1Map
			# 8 Mask2Map
			# 11 for 3D LUT, cube maps and other merged textures
		unk4 = texture_file.read_uint_32()  # range 0-5
		self.bit_field = texture_file.read_uint_32()  # a large number (may be a bit field)
		unk6 = texture_file.read_uint_32()  # seems to always be 0
		unk7 = texture_file.read_uint_32()  # seems to always be 0
		unk8 = texture_file.read_uint_32()  # seems to always be 0

		texture_file.read_id()
		texture_file.read_type()
		one = texture_file.read_uint_32()   # always 1
		seven = texture_file.read_uint_32() # always 7
		dwWidth = texture_file.read_bytes(4)
		dwHeight = texture_file.read_bytes(4)
		dwDepth = texture_file.read_bytes(4)
		mipmapcount = texture_file.read_bytes(4)
		imgDXT = texture_file.read_uint_32()

		unk9 = texture_file.read_uint_32()  # looks to equal unk1
		unk10 = texture_file.read_uint_32()  # looks to equal unk2
		unk11 = texture_file.read_uint_32()  # always 0
		unk12 = texture_file.read_uint_32()  # always 0
		unk13 = texture_file.read_uint_32()  # always 0

		# print(unk1, unk2, self.material_type, unk4, f"{unk5:032b}")

		#logging.info(f'{unk1}	{unk2}	{self.material_type}	{unk4}	{unk5}	{unk6}	{unk7}	{unk8}	{unk9}	{unk10}	{unk11} {unk12}	{unk13} {one}	{seven}    [{dwWidth == self.dwWidth} {dwHeight == self.dwHeight}  {dwDepth == self.dwDepth}  {mipmapcount == self.dwMipMapCount}  {imgDXT == self.imgDXT}]')

		self.dwPitchOrLinearSize = texture_file.read_bytes(4)
		self.buffer = texture_file.read_bytes(struct.unpack('<I', self.dwPitchOrLinearSize)[0])
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
