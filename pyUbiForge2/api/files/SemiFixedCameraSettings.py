from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCameraSettings import TargetEulerCameraSettings as _TargetEulerCameraSettings


class SemiFixedCameraSettings(SubclassBaseFile):
    ResourceType = 0x6A71A2FD
    ParentResourceType = _TargetEulerCameraSettings.ResourceType
    parent: _TargetEulerCameraSettings

