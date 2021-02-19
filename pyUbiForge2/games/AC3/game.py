from ..AC2R import AC2RGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1c


class AC3Game(AC2RGame):
    ForgeClass = ForgeV1c
    GameIdentifier = "AC3"
    FileIDType = "Q"
    ResourceDType = "I"
