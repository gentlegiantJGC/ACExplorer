from pyUbiForge2.api import BaseGame

from .forge import ACUForge


class ACUGame(BaseGame):
    ForgeClass = ACUForge
    GameIdentifier = "ACU"
    FileIDType = "Q"
    ResourceType = "I"
