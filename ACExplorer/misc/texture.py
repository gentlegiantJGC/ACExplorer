import os
import struct


class BaseTexture:
	def __init__(self, app):
		self.app = app
		self.dwSize = '\x7C\x00\x00\x00'  # 124
		DDSD_CAPS = DDSD_HEIGHT = DDSD_WIDTH = DDSD_PIXELFORMAT = True
		# (probably should be set based on the data)
		DDSD_PITCH = False
		DDSD_MIPMAPCOUNT = True
		DDSD_LINEARSIZE = True
		DDSD_DEPTH = False
		self.dwFlags = struct.pack('<i', (0x1*DDSD_CAPS)|(0x2*DDSD_HEIGHT)|(0x4*DDSD_WIDTH)|(0x8*DDSD_PITCH)|(0x1000*DDSD_PIXELFORMAT)|(0x20000*DDSD_MIPMAPCOUNT)|(0x80000*DDSD_LINEARSIZE)|(0x800000*DDSD_DEPTH))
		self.dwWidth = '\x00\x00\x00\x00'
		self.dwHeight = '\x00\x00\x00\x00'
		self.dwDepth = '\x00\x00\x00\x00'
		self.imgDXT = 0
		self.dwMipMapCount = '\x00\x00\x00\x00'
		self.dwPitchOrLinearSize = '\x00\x00\x00\x00'
		self.buffer = ''
		self.dwReserved = '\x00\x00\x00\x00'*11

		self.ddspf = ''  # (pixel format)
		self.ddspf += '\x20\x00\x00\x00'  # dwSize
		self.ddspf += '\x00\x00\x00\x00'
		self.ddspf += 'DXT1'
		self.ddspf += '\x00\x00\x00\x00' * 5  # dwRGBBitCount, dwRBitMask, dwGBitMask, dwBBitMask, dwABitMask
		self.DXT10Header = ''
		self.dwCaps = '\x08\x10\x40\x00'
		self.dwCaps2 = '\x00\x00\x00\x00'
		self.dwCaps3 = '\x00\x00\x00\x00'
		self.dwCaps4 = '\x00\x00\x00\x00'
		self.dwReserved2 = '\x00\x00\x00\x00'

	def export_dds(self, path):
		fi = open(path, 'wb')
		fi.write('DDS ')
		fi.write(self.dwSize + self.dwFlags + self.dwHeight + self.dwWidth +
				 self.dwPitchOrLinearSize + self.dwDepth + self.dwMipMapCount +
				 self.dwReserved + self.ddspf + self.dwCaps + self.dwCaps2 +
				 self.dwCaps3 + self.dwCaps4 + self.dwReserved2 + self.DXT10Header)
		fi.write(self.buffer)
		fi.close()

		if self.imgDXT == 8:
			texconv = '"{}" -fl 9.1 -y -px {}{} -f BC3_UNORM {}'.format(self.app.CONFIG['texconv'], self.app.CONFIG['dumpFolder'], os.sep, path)
			os.system(texconv)
