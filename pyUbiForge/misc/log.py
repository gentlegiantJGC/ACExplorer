class Logger:
	"""The logging module. Used to print messages to the console and log to the log file"""
	def __init__(self, py_ubi_forge):
		self.pyUbiForge = py_ubi_forge
		self.logFile = open(py_ubi_forge.CONFIG['logFile'], 'w')

	def warn(self, name: str, msg: str):
		"""Log with the warning prefix"""
		print(msg)
		self.logFile.write(f'[WARNING]:[{name}]:[{msg}]\n')

	def info(self, name: str, msg: str):
		"""Log with the info prefix"""
		print(msg)
		self.logFile.write(f'[INFO]:[{name}]:[{msg}]\n')
