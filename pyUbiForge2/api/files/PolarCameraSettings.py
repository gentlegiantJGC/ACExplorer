from pyUbiForge2.api.game import SubclassBaseFile
from .TargetCameraSettings import TargetCameraSettings as _TargetCameraSettings


class PolarCameraSettings(SubclassBaseFile):
    ResourceType = 0xF38E61D4
    ParentResourceType = _TargetCameraSettings.ResourceType
    parent: _TargetCameraSettings

