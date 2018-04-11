from ctypes import CDLL, c_ubyte, c_ushort
from ACExplorer import CONFIG
import platform
if platform.architecture()[0] == '64bit':
	lzoPath = CONFIG['LZO64Path'].encode('utf-8')
elif platform.architecture()[0] == '32bit':
	lzoPath = CONFIG['LZO32Path'].encode('utf-8')
else:
	raise Exception('Unknown Architecture')


def decompress(mode, src, dst_len):
	lzo = CDLL(lzoPath)
	src = [ord(x) for x in src]
	src = (c_ubyte * len(src))(*src)
	src_len = (c_ushort*1)(len(src))
	dst = (c_ubyte * dst_len)()
	dst_len = (c_ushort*1)(dst_len)
	workMem = (c_ubyte * 65536)()
	if mode in [0,1]:
		#lzo1x
		lzo.lzo1x_decompress(src, src_len, dst, dst_len, workMem)
	elif mode == 2:
		#lzo2a
		lzo.lzo2a_decompress(src, src_len, dst, dst_len, workMem)
	elif mode == 5:
		#lzo1c
		lzo.lzo1c_decompress(src, src_len, dst, dst_len, workMem)
	dst = ''.join([chr(x) for x in dst])
	return dst
