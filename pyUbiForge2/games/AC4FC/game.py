from pyUbiForge2.api import BaseGame
from .forge import AC4FCForge


class AC4FCGame(BaseGame):
    ForgeClass = AC4FCForge
    GameIdentifier = "AC4FC"
    FileIDType = "Q"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
