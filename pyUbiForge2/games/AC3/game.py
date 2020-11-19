from pyUbiForge2.api import BaseGame
from pyUbiForge2.api.game.forge.forge_v1 import ForgeV1b


class AC3Game(BaseGame):
    ForgeClass = ForgeV1b
    GameIdentifier = "AC3"
    FileIDType = "Q"
    ResourceType = "I"
