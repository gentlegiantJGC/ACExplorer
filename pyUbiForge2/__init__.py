import os

CACHE_DIR = os.path.join(os.path.dirname(__file__), "cache")

from pyUbiForge2.api import BaseGame, BaseForge, DataFile, BaseFile, FileDataWrapper

from .games import GAMES
