import os
import struct


class BaseTexture:
	def __init__(self, app):
		self.app = app
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

	def export_dds(self, path):
		fi = open(path, 'wb')
		fi.write(b'DDS ')
		fi.write(self.dwSize + self.dwFlags + self.dwHeight + self.dwWidth +
				 self.dwPitchOrLinearSize + self.dwDepth + self.dwMipMapCount +
				 self.dwReserved + self.ddspf + self.dwCaps + self.dwCaps2 +
				 self.dwCaps3 + self.dwCaps4 + self.dwReserved2 + self.DXT10Header)
		fi.write(self.buffer)
		fi.close()

		if self.imgDXT == 8:
			texconv = '"{}" -fl 9.1 -y -px {}{} -f BC3_UNORM {}'.format(self.app.CONFIG['texconv'], self.app.CONFIG['dumpFolder'], os.sep, path)
			os.system(texconv)


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


def export_dds(app, file_id, save_folder):
	data = app.tempNewFiles.get_data(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return
	texture_file = data["rawFile"]
	save_path = os.path.join(save_folder, '{}.dds'.format(data['fileName']))
	if os.path.isfile(save_path):
		app.log.info(__name__, 'Texture "{}" already exported'.format(data['fileName']))
		return save_path
	tex = app.read_file.get_data(texture_file)
	tex.export_dds(save_path)
	app.log.info(__name__, 'Texture "{}" exported'.format(data['fileName']))
	return save_path
