from pyUbiForge2.api import BaseGame
from .forge import AC2Forge


class AC2Game(BaseGame):
    ForgeClass = AC2Forge
    GameIdentifier = "AC2"
    FileIDType = "I"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
