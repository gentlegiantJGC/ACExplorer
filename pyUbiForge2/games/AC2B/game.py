from pyUbiForge2.api import BaseGame
from .forge import AC2BForge


class AC2BGame(BaseGame):
    ForgeClass = AC2BForge
    GameIdentifier = "AC2B"
    FileIDType = "I"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
