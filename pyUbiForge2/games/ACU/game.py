from pyUbiForge2.api import BaseGame

from .forge import ACUForge


class ACUGame(BaseGame):
    ForgeClass = ACUForge
    GameIdentifier = "ACU"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000):
        super().__init__(game_directory, cache_megabytes)
