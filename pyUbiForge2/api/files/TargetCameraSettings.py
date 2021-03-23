from pyUbiForge2.api.game import SubclassBaseFile
from .CameraSettings import CameraSettings as _CameraSettings


class TargetCameraSettings(SubclassBaseFile):
    ResourceType = 0xC1ED0186
    ParentResourceType = _CameraSettings.ResourceType
    parent: _CameraSettings

