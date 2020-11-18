from pyUbiForge2.api import BaseGame
from .forge import AC3Forge


class AC3Game(BaseGame):
    ForgeClass = AC3Forge
    GameIdentifier = "AC3"
    FileIDType = "Q"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
