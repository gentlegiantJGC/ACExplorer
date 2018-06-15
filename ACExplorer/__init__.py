import json, sys

try:
	with open("config.json") as f:
		CONFIG = json.load(f)
except:
	CONFIG = {
		"LZO32Path": "resources\\lzo32.dll",
		"LZO64Path": "resources\\lzo64.dll",
		"texconv": "resources\\texconv.exe",
		"missingNo": "resources\\missingNo.png",

		"lightDict": "",
		"ACUnityFolder": "",

		"dumpFolder": "",

		"logFile": "ACExplorer.log",

	}

dev = 'dev' in sys.argv
if dev:
	formatLog = {}