import binascii, struct


def BEHEX(f, start, length):
	# given a string object
	# will convert to hex format
	# used for extracting file types
	be = binascii.hexlify(f[start:start+length]).upper()
	return be
	
def BEHEX2(f):
	# converts whole string to hex text
	be = binascii.hexlify(f).upper()
	return be
	
def LE2BE(f, start, length):
	# given a string object
	# will convert from little endian to big endian
	be = binascii.hexlify(f[start:start+length][::-1]).upper()
	return be
	
def LE2BE2(f):
	# given a string object
	# converts the whole string from little endian to big endian
	be = binascii.hexlify(f[::-1]).upper()
	return be
	
def LE2DEC(f, start, length):
	# given a string object
	# return the base 10 version of a little endian stored value
	dec = int(binascii.hexlify(f[start:start+length][::-1]), 16)
	return dec
	
def LE2DEC2(f):
	# given a string object
	# converts the whole string to base 10
	dec = int(binascii.hexlify(f[::-1]), 16)
	return dec
	
def BE(f, start, length):
	# given string object
	# extracts a string from the string
	# used to extract file names
	be = f[start:start+length]
	return be


'''preferentially use the below functions over the above'''


def int16(f):
	# given a binary string object of length 4
	# converts from a little endian signed short to base 10
	if type(f) == file:
		f = f.read(2)
	if len(f) == 2:
		return struct.unpack('<h',f)[0]
	else:
		raise Exception('int16 can only accept 16 bits (2 bytes)')

def uint16(f):
	# given a binary string object of length 4
	# converts from a little endian unsigned short to base 10
	if type(f) == file:
		f = f.read(2)
	if len(f) == 2:
		return struct.unpack('<H',f)[0]
	else:
		raise Exception('uint16 can only accept 16 bits (2 bytes)')

def int32(f):
	# given a binary string object of length 4
	# converts from a little endian signed int to base 10
	if type(f) == file:
		f = f.read(4)
	if len(f) == 4:
		return struct.unpack('<i',f)[0]
	else:
		raise Exception('int32 can only accept 32 bits (4 bytes)')

def uint32(f):
	# given a binary string object of length 4
	# converts from a little endian unsigned int to base 10
	if type(f) == file:
		f = f.read(4)
	if len(f) == 4:
		return struct.unpack('<I',f)[0]
	else:
		raise Exception('uint32 can only accept 32 bits (4 bytes)')

def int64(f):
	# given a binary string object of length 8
	# converts from a little endian signed int to base 10
	if type(f) == file:
		f = f.read(8)
	if len(f) == 8:
		return struct.unpack('<q',f)[0]
	else:
		raise Exception('int32 can only accept 32 bits (4 bytes)')

def uint64(f):
	# given a binary string object of length 8
	# converts from a little endian unsigned int to base 10
	if type(f) == file:
		f = f.read(8)
	if len(f) == 8:
		return struct.unpack('<Q',f)[0]
	else:
		raise Exception('uint32 can only accept 32 bits (4 bytes)')

def float32(f):
	# given string object
	# converts from little endian to big endian
	# converts from hex representation of 32 bit signed float to float
	if type(f) == file:
		f = f.read(4)
	if len(f) == 4:
		return struct.unpack('<f',f)[0]
	else:
		raise Exception('float32 can only accept 32 bits (4 bytes)')