import os
import json

PathsFile = os.path.join(os.path.dirname(__file__), "game_paths.json")

_game_paths = {}
if os.path.isfile(PathsFile):
    try:
        with open(PathsFile) as f:
            _game_paths = json.load(f)
    except:
        pass
    if not isinstance(_game_paths, dict):
        _game_paths = {}


AC1Path = _game_paths.get("AC1Path")
PoPPath = _game_paths.get("PoPPath")
SWPath = _game_paths.get("SWPath")
AC2Path = _game_paths.get("AC2Path")
PoPFSPath = _game_paths.get("PoPFSPath")
AC2BPath = _game_paths.get("AC2BPath")
AC2BMPPath = _game_paths.get("AC2BMPPath")
AC2RPath = _game_paths.get("AC2RPath")
AC2RMPPath = _game_paths.get("AC2RMPPath")
AC3Path = _game_paths.get("AC3Path")
AC3MPPath = _game_paths.get("AC3MPPath")
AC3LPath = _game_paths.get("AC3LPath")
AC4Path = _game_paths.get("AC4Path")
AC4MPPath = _game_paths.get("AC4MPPath")
AC4FCPath = _game_paths.get("AC4FCPath")
ACRoPath = _game_paths.get("ACRoPath")
ACUPath = _game_paths.get("ACUPath")
ACSPath = _game_paths.get("ACSPath")
TCSSPath = _game_paths.get("TCSSPath")
StPath = _game_paths.get("StPath")
FHPath = _game_paths.get("FHPath")
TCWPath = _game_paths.get("TCWPath")
ACOPath = _game_paths.get("ACOPath")
ACDTEPath = _game_paths.get("ACDTEPath")
ACOdPath = _game_paths.get("ACOdPath")
ACDTGPath = _game_paths.get("ACDTGPath")
TCBPath = _game_paths.get("TCBPath")
HSPath = _game_paths.get("HSPath")
ACVPath = _game_paths.get("ACVPath")
