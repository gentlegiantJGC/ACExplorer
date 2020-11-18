from pyUbiForge2.api import BaseGame
from .forge import AC1Forge


class AC1Game(BaseGame):
    ForgeClass = AC1Forge
    GameIdentifier = "AC1"
    FileIDType = "I"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
