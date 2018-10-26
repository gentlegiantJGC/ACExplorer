import os


class FileObject:
	def __init__(self, path=None, mode='w'):
		self.path = None
		self.mode = None
		self.data = ''
		if path is not None:
			if 'r' in mode:
				with open(path, mode) as f:
					self.data = f.read()
			else:
				self.data = ''
				self.path = path
				self.mode = mode
		self.filePointer = 0

	def tell(self):
		return self.filePointer

	def write(self, s):
		self.data += s
		self.filePointer += len(s)

	def read(self, length='end'):
		if length == 'end':
			data = self.data[self.filePointer:]
			self.filePointer = len(self.data)
			return data
		elif isinstance(length, int):
			data = self.data[self.filePointer:self.filePointer + length]
			self.filePointer += length
			return data
		else:
			raise Exception('Unsupported type: "{}"'.format(type(length)))

	def seek(self, offset, whence=0):
		if whence == 0:
			self.filePointer = offset
		elif whence == 1:
			self.filePointer += offset
		elif whence == 2:
			self.filePointer = len(self.data) - offset

	def save(self, path=None, mode=None):
		if path is not None:
			self.path = path
		if mode is not None:
			self.mode = mode
		if self.mode in 'wa':
			if not os.path.isdir(os.path.dirname(self.path)):
				os.makedirs(os.path.dirname(self.path))
			with open(self.path, self.mode) as f:
				f.write(self.data)
