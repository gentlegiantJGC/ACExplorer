from pyUbiForge2.api import BaseGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1a


class AC1Game(BaseGame):
    ForgeClass = ForgeV1a
    GameIdentifier = "AC1"
    FileIDType = "I"
    ResourceDType = "I"
