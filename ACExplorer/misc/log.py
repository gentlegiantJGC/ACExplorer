from ACExplorer import CONFIG

logFile = open(CONFIG['logFile'], 'w')

def warn(name, msg):
	print msg
	logFile.write('[WARNING]:['+str(name)+']:'+msg)
	logFile.write('\n')

def info(name, msg):
	print msg
	logFile.write('[INFO]:['+str(name)+']:'+msg)
	logFile.write('\n')