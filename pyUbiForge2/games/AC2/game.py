from pyUbiForge2.api import BaseGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1b


class AC2Game(BaseGame):
    ForgeClass = ForgeV1b
    GameIdentifier = "AC2"
    FileIDType = "I"
    ResourceType = "I"
