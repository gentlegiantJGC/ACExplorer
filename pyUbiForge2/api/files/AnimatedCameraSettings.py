from pyUbiForge2.api.game import SubclassBaseFile
from .CameraSettings import CameraSettings as _CameraSettings


class AnimatedCameraSettings(SubclassBaseFile):
    ResourceType = 0x63BF395D
    ParentResourceType = _CameraSettings.ResourceType
    parent: _CameraSettings

