from pyUbiForge2.api.game import SubclassBaseFile
from .FreeRoamingCamera2 import FreeRoamingCamera2 as _FreeRoamingCamera2


class AC2FreeRoamingCamera(SubclassBaseFile):
    ResourceType = 0x6CC7B1AB
    ParentResourceType = _FreeRoamingCamera2.ResourceType
    parent: _FreeRoamingCamera2

