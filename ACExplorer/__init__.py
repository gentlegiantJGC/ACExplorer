import json, sys

try:
	with open("config.json") as f:
		CONFIG = json.load(f)
except:
	CONFIG = {}

defaultConfig = {
	"LZO32Path": "resources\\lzo32.dll",
	"LZO64Path": "resources\\lzo64.dll",
	"texconv": "resources\\texconv.exe",
	"missingNo": "resources\\missingNo.png",

	"lightDict": "",
	"ACUnityFolder": "",

	"dumpFolder": "",

	"logFile": "ACExplorer.log",
	"tempFilesMaxMemoryMB": 2048,
	"writeToDisk": False
}

for key, val in defaultConfig.iteritems():
	if key not in CONFIG:
		CONFIG[key] = val

dev = 'dev' in sys.argv
if dev:
	formatLog = {}