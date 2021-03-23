from pyUbiForge2.api.game import SubclassBaseFile
from .FreeRoamingCameraSettings import (
    FreeRoamingCameraSettings as _FreeRoamingCameraSettings,
)


class LowHighProfileCameraSettings(SubclassBaseFile):
    ResourceType = 0x78A6DEFF
    ParentResourceType = _FreeRoamingCameraSettings.ResourceType
    parent: _FreeRoamingCameraSettings
