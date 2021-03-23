from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCameraSettings import TargetEulerCameraSettings as _TargetEulerCameraSettings


class FixedCameraSettings(SubclassBaseFile):
    ResourceType = 0xA59C54C0
    ParentResourceType = _TargetEulerCameraSettings.ResourceType
    parent: _TargetEulerCameraSettings

