from pyUbiForge2.api import BaseGame
from .forge import AC2RForge


class AC2RGame(BaseGame):
    ForgeClass = AC2RForge
    GameIdentifier = "AC2R"
    FileIDType = "I"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
