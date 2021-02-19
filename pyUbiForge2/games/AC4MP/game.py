from pyUbiForge2.api import BaseGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1b


class AC4MPGame(BaseGame):
    ForgeClass = ForgeV1b
    GameIdentifier = "AC4MP"
    FileIDType = "I"
    ResourceDType = "I"
