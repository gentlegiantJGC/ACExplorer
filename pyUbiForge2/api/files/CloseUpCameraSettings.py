from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCameraSettings import (
    ThirdPersonCameraSettings as _ThirdPersonCameraSettings,
)


class CloseUpCameraSettings(SubclassBaseFile):
    ResourceType = 0xB355AD3E
    ParentResourceType = _ThirdPersonCameraSettings.ResourceType
    parent: _ThirdPersonCameraSettings
