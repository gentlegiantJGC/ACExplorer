from pyUbiForge2.api.game import SubclassBaseFile
from .FreeRoamingCameraSettings import FreeRoamingCameraSettings as _FreeRoamingCameraSettings


class HorseCameraSettings(SubclassBaseFile):
    ResourceType = 0x01FCAD18
    ParentResourceType = _FreeRoamingCameraSettings.ResourceType
    parent: _FreeRoamingCameraSettings

