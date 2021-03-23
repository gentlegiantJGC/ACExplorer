from pyUbiForge2.api.game import SubclassBaseFile
from .CameraSettings import CameraSettings as _CameraSettings


class BlendCameraSettings(SubclassBaseFile):
    ResourceType = 0xF73A2917
    ParentResourceType = _CameraSettings.ResourceType
    parent: _CameraSettings
