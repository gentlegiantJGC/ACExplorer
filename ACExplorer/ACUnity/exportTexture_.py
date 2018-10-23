import os
import struct
from ACExplorer.misc import BaseTexture
from ACExplorer.misc.dataTypes import LE2DEC2
from ACExplorer.ACUnity.formatFile import readStr

class Texture(BaseTexture):
	def __init__(self, app, fi):
		BaseTexture.__init__(self, app)
		try:
			with open(os.path.join(app.CONFIG['dumpFolder'], 'fileTypes', 'A2B7E917'), 'a') as f2:
				readStr(fi, f2, 130)
		except:
			print 'fail'
		fi.seek(0)
		fi.seek(14)
		self.dwSize = '\x7C\x00\x00\x00' #124
		DDSD_CAPS = DDSD_HEIGHT = DDSD_WIDTH = DDSD_PIXELFORMAT = True
		#(probably should be set based on the data)
		DDSD_PITCH = False
		DDSD_MIPMAPCOUNT = True
		DDSD_LINEARSIZE = True
		DDSD_DEPTH = False
		self.dwFlags = struct.pack('<i', (0x1*DDSD_CAPS)|(0x2*DDSD_HEIGHT)|(0x4*DDSD_WIDTH)|(0x8*DDSD_PITCH)|(0x1000*DDSD_PIXELFORMAT)|(0x20000*DDSD_MIPMAPCOUNT)|(0x80000*DDSD_LINEARSIZE)|(0x800000*DDSD_DEPTH))
		self.dwWidth = fi.read(4)
		self.dwHeight = fi.read(4)
		self.dwDepth = fi.read(4)
		self.imgDXT = LE2DEC2(fi.read(4))
		fi.seek(8, 1)   # could be image format. Volume textures have first 4 \x03\x00\x00\x00 all else have \x01\x00\x00\x00
						# next 4 are \x01\x00\x00\x00 for diffuse maps and \x00\x00\x00\x00 for other things like volume textures and maps
		self.dwMipMapCount = fi.read(4)
		fi.seek(84, 1)  #24 of other data followed by "CompiledTextureMap" which duplicates most of the data
		self.dwPitchOrLinearSize = fi.read(4)
		self.buffer = fi.read(LE2DEC2(self.dwPitchOrLinearSize))
		self.dwReserved = '\x00\x00\x00\x00'*11

		self.ddspf = '' #(pixel format)
		self.ddspf += '\x20\x00\x00\x00'    #dwSize
		if self.imgDXT in [0,7]:    #dwFlags
			self.ddspf += '\x40\x00\x00\x00'
		else:
			self.ddspf += '\x04\x00\x00\x00'
		# if imgDXT in [0, 7]:
		# 	self.ddspf += 'DXT1'
		if self.imgDXT in [0, 1, 2, 3, 7]: #dwFourCC
			self.ddspf += 'DXT1'
		elif self.imgDXT == 4:
			self.ddspf += 'DXT3'
		elif self.imgDXT in [5, 6]:
			self.ddspf += 'DXT5'
		elif self.imgDXT in [8, 9, 16]:
			self.ddspf += 'DX10'
		else:
			raise Exception('imgDXT: "{}" is not currently supported'.format(self.imgDXT))

		self.ddspf += '\x00\x00\x00\x00' * 5    #dwRGBBitCount, dwRBitMask, dwGBitMask, dwBBitMask, dwABitMask
		if self.imgDXT == 8:
			self.DXT10Header = '\x62\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
		else:
			self.DXT10Header = ''
		self.dwCaps = '\x08\x10\x40\x00'
		self.dwCaps2 = '\x00\x00\x00\x00'
		self.dwCaps3 = '\x00\x00\x00\x00'
		self.dwCaps4 = '\x00\x00\x00\x00'
		self.dwReserved2 = '\x00\x00\x00\x00'

def export_texture(app, fileID):
	data = app.tempNewFiles.getData(fileID)
	if data is None:
		app.log.warn(__name__, "Failed to find file {}".format(fileID))
		return
	fi = app.misc.fileObject()
	fi.write(data["rawFile"])
	save_path = os.path.join(app.CONFIG['dumpFolder'], '{}.dds'.format(data['fileName']))
	if os.path.isfile(save_path):
		return save_path
	tex = Texture(app, fi)
	tex.exportDDS(save_path)
	return save_path
