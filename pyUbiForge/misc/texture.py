import os
import struct
from typing import Union
import logging
import pyUbiForge
from pyUbiForge.misc import texconv


class BaseTexture:
	def __init__(self):
		self.dwSize = b'\x7C\x00\x00\x00'  # 124
		DDSD_CAPS = DDSD_HEIGHT = DDSD_WIDTH = DDSD_PIXELFORMAT = True
		# (probably should be set based on the data)
		DDSD_PITCH = False
		DDSD_MIPMAPCOUNT = True
		DDSD_LINEARSIZE = True
		DDSD_DEPTH = False
		self.dwFlags = struct.pack('<i', (0x1*DDSD_CAPS)|(0x2*DDSD_HEIGHT)|(0x4*DDSD_WIDTH)|(0x8*DDSD_PITCH)|(0x1000*DDSD_PIXELFORMAT)|(0x20000*DDSD_MIPMAPCOUNT)|(0x80000*DDSD_LINEARSIZE)|(0x800000*DDSD_DEPTH))
		self.dwWidth = b'\x00\x00\x00\x00'
		self.dwHeight = b'\x00\x00\x00\x00'
		self.dwDepth = b'\x00\x00\x00\x00'
		self.imgDXT = 0
		self.dwMipMapCount = b'\x00\x00\x00\x00'
		self.dwPitchOrLinearSize = b'\x00\x00\x00\x00'
		self.buffer = b''
		self.dwReserved = b'\x00\x00\x00\x00'*11

		self.ddspf = b''  # (pixel format)
		self.ddspf += b'\x20\x00\x00\x00'  # dwSize
		self.ddspf += b'\x00\x00\x00\x00'
		self.ddspf += b'DXT1'
		self.ddspf += b'\x00\x00\x00\x00' * 5  # dwRGBBitCount, dwRBitMask, dwGBitMask, dwBBitMask, dwABitMask
		self.DXT10Header = b''
		self.dwCaps = b'\x08\x10\x40\x00'
		self.dwCaps2 = b'\x00\x00\x00\x00'
		self.dwCaps3 = b'\x00\x00\x00\x00'
		self.dwCaps4 = b'\x00\x00\x00\x00'
		self.dwReserved2 = b'\x00\x00\x00\x00'

	@property
	def dds_string(self):
		return b'DDS ' + self.dwSize + self.dwFlags + self.dwHeight + self.dwWidth + self.dwPitchOrLinearSize +\
			self.dwDepth + self.dwMipMapCount + self.dwReserved + self.ddspf + self.dwCaps + self.dwCaps2 + \
			self.dwCaps3 + self.dwCaps4 + self.dwReserved2 + self.DXT10Header + self.buffer

	def export_dds(self, path):
		with open(path, 'wb') as fi:
			fi.write(self.dds_string)

		if self.imgDXT == 8:
			arg = f'-fl 9.1 -y -o {os.path.dirname(path)} -f BC3_UNORM {path}'
			texconv.convert_texture(arg)


class Material:
	def __init__(self, name, missing_no=False, diffuse=None, normal=None, specular=None, height=None, transmission=None, mask1=None, mask2=None):
		self.name = name
		self.missing_no = missing_no
		self.diffuse = diffuse
		self.normal = normal
		self.specular = specular
		self.height = height
		self.transmission = transmission
		self.mask1 = mask1
		self.mask2 = mask2


def export_dds(file_id: int, save_folder: str, forge_file_name: Union[None, str]=None, datafile_id: Union[None, int]=None):
	data = pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)
	if data is None:
		logging.warning(f"Failed to find file {file_id:016X}")
		return
	save_path = os.path.join(save_folder, f'{data.file_name}.dds')
	if os.path.isfile(save_path):
		logging.info(f'Texture "{data.file_name}" already exported')
		return save_path
	tex = pyUbiForge.read_file(data.file)
	tex.export_dds(save_path)
	logging.info(f'Texture "{data.file_name}" exported')
	return save_path
