from pyUbiForge2.api.game import SubclassBaseFile
from .FreeRoamingCamera2 import FreeRoamingCamera2 as _FreeRoamingCamera2


class GhostCamera(SubclassBaseFile):
    ResourceType = 0x62949FAA
    ParentResourceType = _FreeRoamingCamera2.ResourceType
    parent: _FreeRoamingCamera2

