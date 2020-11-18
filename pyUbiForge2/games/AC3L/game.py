from pyUbiForge2.api import BaseGame
from .forge import AC3LForge


class AC3LGame(BaseGame):
    ForgeClass = AC3LForge
    GameIdentifier = "AC3L"
    FileIDType = "Q"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
