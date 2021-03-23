from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEulerCameraSettings import TargetEulerCameraSettings as _TargetEulerCameraSettings


class PointAxisCameraSettings(SubclassBaseFile):
    ResourceType = 0x0B1EC826
    ParentResourceType = _TargetEulerCameraSettings.ResourceType
    parent: _TargetEulerCameraSettings

