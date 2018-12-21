class Logger:
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self.logFile = open(py_ubi_forge.CONFIG['logFile'], 'w')

	def warn(self, name, msg):
		print(msg)
		self.logFile.write(f'[WARNING]:[{name}]:[{msg}]\n')

	def info(self, name, msg):
		print(msg)
		self.logFile.write(f'[INFO]:[{name}]:[{msg}]\n')
