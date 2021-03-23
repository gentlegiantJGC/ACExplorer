from pyUbiForge2.api.game import SubclassBaseFile
from .FreeRoamingCamera import FreeRoamingCamera as _FreeRoamingCamera


class HorseCamera(SubclassBaseFile):
    ResourceType = 0x8F964249
    ParentResourceType = _FreeRoamingCamera.ResourceType
    parent: _FreeRoamingCamera

