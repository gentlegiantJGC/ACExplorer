from ctypes import CDLL, c_ushort
import platform
if platform.architecture()[0] == '64bit':
	lzoPath = "resources\\lzo64.dll".encode('utf-8')
elif platform.architecture()[0] == '32bit':
	lzoPath = "resources\\lzo32.dll".encode('utf-8')
else:
	raise Exception('Unknown Architecture')

lzo = CDLL(lzoPath)


def decompress(mode, src, dst_len):
	if len(src) == dst_len:
		return src
	src_len = (c_ushort*1)(len(src))
	dst = '\x00' * dst_len
	dst_len = (c_ushort*1)(dst_len)
	if mode in [0, 1]:
		# lzo1x
		lzo.lzo1x_decompress(src, src_len, dst, dst_len, None)
	elif mode == 2:
		# lzo2a
		lzo.lzo2a_decompress(src, src_len, dst, dst_len, None)
	elif mode == 5:
		# lzo1c
		lzo.lzo1c_decompress(src, src_len, dst, dst_len, None)
	else:
		raise Exception('Decompression Mode "{}" is not supported'.format(mode))
	return dst
