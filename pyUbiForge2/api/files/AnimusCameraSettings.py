from pyUbiForge2.api.game import SubclassBaseFile
from .FixedCameraSettings import FixedCameraSettings as _FixedCameraSettings


class AnimusCameraSettings(SubclassBaseFile):
    ResourceType = 0xD5402DD9
    ParentResourceType = _FixedCameraSettings.ResourceType
    parent: _FixedCameraSettings
