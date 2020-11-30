from pyUbiForge2.api import BaseGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1b


class AC2RMPGame(BaseGame):
    ForgeClass = ForgeV1b
    GameIdentifier = "AC2RMP"
    FileIDType = "I"
    ResourceType = "I"
