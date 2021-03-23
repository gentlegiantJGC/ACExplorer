from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCameraSettings import (
    ThirdPersonCameraSettings as _ThirdPersonCameraSettings,
)


class SweetCameraSettings(SubclassBaseFile):
    ResourceType = 0xFE5709C1
    ParentResourceType = _ThirdPersonCameraSettings.ResourceType
    parent: _ThirdPersonCameraSettings
