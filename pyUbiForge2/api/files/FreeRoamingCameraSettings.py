from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCameraSettings import (
    ThirdPersonCameraSettings as _ThirdPersonCameraSettings,
)


class FreeRoamingCameraSettings(SubclassBaseFile):
    ResourceType = 0x19B62C56
    ParentResourceType = _ThirdPersonCameraSettings.ResourceType
    parent: _ThirdPersonCameraSettings
