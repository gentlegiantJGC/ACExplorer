from ..AC1 import AC1Game
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1b


class AC2Game(AC1Game):
    ForgeClass = ForgeV1b
    GameIdentifier = "AC2"
