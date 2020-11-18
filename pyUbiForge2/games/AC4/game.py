from pyUbiForge2.api import BaseGame
from .forge import AC4Forge


class AC4Game(BaseGame):
    ForgeClass = AC4Forge
    GameIdentifier = "AC4"
    FileIDType = "Q"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
