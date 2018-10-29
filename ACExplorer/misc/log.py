class logger:
	def __init__(self, app):
		self.app = app
		self.logFile = open(app.CONFIG['logFile'], 'w')
	def warn(self, name, msg):
		print(msg)
		self.logFile.write('[WARNING]:[{}]:'.format(name, msg))
		self.logFile.write('\n')

	def info(self, name, msg):
		print(msg)
		self.logFile.write('[INFO]:[{}]:'.format(name, msg))
		self.logFile.write('\n')