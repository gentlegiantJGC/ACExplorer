class Logger:
	"""The logging module. Used to print messages to the console and log to the log file"""
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self.logFile = open(py_ubi_forge.CONFIG['logFile'], 'w')
		self.buffer = None

	def warn(self, name: str, msg: str):
		"""Log with the warning prefix"""
		self.logFile.write(f'[WARNING]:[{name}]:[{msg}]\n')
		if self.pyUbiForge.CONFIG.get('dev', False):
			print(msg)
			self.buffer = msg

	def info(self, name: str, msg: str):
		"""Log with the info prefix"""
		self.logFile.write(f'[INFO]:[{name}]:[{msg}]\n')
		print(msg)
		self.buffer = msg
