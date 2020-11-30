from pyUbiForge2.api import BaseGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1c


class AC3LGame(BaseGame):
    ForgeClass = ForgeV1c
    GameIdentifier = "AC3L"
    FileIDType = "Q"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)