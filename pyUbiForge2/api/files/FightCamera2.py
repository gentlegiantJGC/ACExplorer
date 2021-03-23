from pyUbiForge2.api.game import SubclassBaseFile
from .FreeRoamingCamera2 import FreeRoamingCamera2 as _FreeRoamingCamera2


class FightCamera2(SubclassBaseFile):
    ResourceType = 0x4BDD6F93
    ParentResourceType = _FreeRoamingCamera2.ResourceType
    parent: _FreeRoamingCamera2

