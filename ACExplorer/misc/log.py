class Logger:
	def __init__(self, app):
		self.app = app
		self.logFile = open(app.CONFIG['logFile'], 'w')

	def warn(self, name, msg):
		print(msg)
		self.logFile.write(f'[WARNING]:[{name}]:[{msg}]\n')

	def info(self, name, msg):
		print(msg)
		self.logFile.write(f'[INFO]:[{name}]:[{msg}]\n')
