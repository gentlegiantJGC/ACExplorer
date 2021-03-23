from pyUbiForge2.api.game import SubclassBaseFile
from .ThirdPersonCameraSettings import (
    ThirdPersonCameraSettings as _ThirdPersonCameraSettings,
)


class InsertCameraSettings(SubclassBaseFile):
    ResourceType = 0xF455DA0D
    ParentResourceType = _ThirdPersonCameraSettings.ResourceType
    parent: _ThirdPersonCameraSettings
