from pyUbiForge2.api.game import SubclassBaseFile
from .FreeRoamingCamera import FreeRoamingCamera as _FreeRoamingCamera


class LowHighProfileCamera(SubclassBaseFile):
    ResourceType = 0x2DCF7371
    ParentResourceType = _FreeRoamingCamera.ResourceType
    parent: _FreeRoamingCamera
