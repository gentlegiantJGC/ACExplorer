from pyUbiForge2.api import BaseGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1b


class AC3MPGame(BaseGame):
    ForgeClass = ForgeV1b
    GameIdentifier = "AC3MP"
    FileIDType = "Q"
    ResourceDType = "I"
