def BEHEX(f, start, length):
	# given a string object
	# will convert to hex format
	# used for extracting file types
	import binascii
	be = binascii.hexlify(f[start:start+length])
	return be
	
def BEHEX2(f):
	# converts whole string to hex text
	import binascii
	be = binascii.hexlify(f)
	return be
	
def LE2BE(f, start, length):
	# given a string object
	# will convert from little endian to big endian
	import binascii
	be = binascii.hexlify(f[start:start+length][::-1])
	return be
	
def LE2BE2(f):
	# given a string object
	# converts the whole string from little endian to big endian
	import binascii
	be = binascii.hexlify(f[::-1])
	return be
	
def LE2DEC(f, start, length):
	# given a string object
	# return the base 10 version of a little endian stored value
	import binascii
	dec = int(binascii.hexlify(f[start:start+length][::-1]), 16)
	return dec
	
def LE2DEC2(f):
	# given a string object
	# converts the whole string to base 10
	import binascii
	dec = int(binascii.hexlify(f[::-1]), 16)
	return dec
	
def BE(f, start, length):
	# given string object
	# extracts a string from the string
	# used to extract file names
	be = f[start:start+length]
	return be
	
def float32(f):
	# given string object
	# converts from little endian to big endian
	# converts from hex representation of 32 bit signed float to float
	import struct
	if len(f) == 4:
		return struct.unpack('<f',f)[0]
	else:
		raise Exception('float32 can only accept 32 bits (4 bytes)')