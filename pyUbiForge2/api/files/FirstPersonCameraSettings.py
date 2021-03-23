from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCameraSettings import (
    TargetEulerCameraSettings as _TargetEulerCameraSettings,
)


class FirstPersonCameraSettings(SubclassBaseFile):
    ResourceType = 0x6B805687
    ParentResourceType = _TargetEulerCameraSettings.ResourceType
    parent: _TargetEulerCameraSettings
