import binascii
from ctypes import CDLL, c_byte, c_ushort

from ACExplorer import CONFIG


def decompress(mode, src, dst_len):
	lzo = CDLL(CONFIG['LZOPath'])
	src = [int(binascii.hexlify(x), 16) for x in src]
	src = (c_byte * len(src))(*src)
	src_len = (c_ushort*1)(len(src))
	dst = (c_byte * dst_len)()
	dst_len = (c_ushort*1)(dst_len)
	workMem = (c_byte * 65536)()
	if mode in [0,1]:
		#lzo1x
		lzo.lzo1x_decompress(src, src_len, dst, dst_len, workMem)
	elif mode == 2:
		#lzo2a
		lzo.lzo2a_decompress(src, src_len, dst, dst_len, workMem)
	elif mode == 5:
		#lzo1c
		lzo.lzo1c_decompress(src, src_len, dst, dst_len, workMem)
	dst = list(dst)
	for c in xrange(len(dst)):
		if dst[c] < 0:
			dst[c] += 256
		dst[c] = chr(dst[c])
	dst = ''.join(dst)
	return dst
