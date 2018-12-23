from ctypes import CDLL, c_ushort
import platform
if platform.architecture()[0] == '64bit':
	lzoPath = "resources/lzo64.dll"
elif platform.architecture()[0] == '32bit':
	lzoPath = "resources/lzo32.dll"
else:
	raise Exception('Unknown Architecture')

lzo = CDLL(lzoPath)


def decompress(mode: int, src: bytes, dst_len: int) -> bytes:
	"""This is the function that does the actual decompression of the data"""
	if len(src) == dst_len:
		return src
	src_len = (c_ushort*1)(len(src))
	dst = b'\x00' * dst_len
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
		raise Exception(f'Decompression Mode "{mode}" is not supported')
	return dst
