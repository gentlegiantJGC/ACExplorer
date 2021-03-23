from pyUbiForge2.api.game import SubclassBaseFile
from .TargetCameraSettings import TargetCameraSettings as _TargetCameraSettings


class TargetEulerCameraSettings(SubclassBaseFile):
    ResourceType = 0xE7D8C234
    ParentResourceType = _TargetCameraSettings.ResourceType
    parent: _TargetCameraSettings
