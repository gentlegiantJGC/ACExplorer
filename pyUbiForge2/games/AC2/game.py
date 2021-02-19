from ..AC1 import AC1Game
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1b
from .files import FileReaders


class AC2Game(AC1Game):
    ForgeClass = ForgeV1b
    GameIdentifier = "AC2"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
        self._file_readers.update(FileReaders)
