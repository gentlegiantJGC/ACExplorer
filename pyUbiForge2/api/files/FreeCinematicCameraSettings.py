from pyUbiForge2.api.game import SubclassBaseFile
from .CameraSettings import CameraSettings as _CameraSettings


class FreeCinematicCameraSettings(SubclassBaseFile):
    ResourceType = 0xF3FB6EC9
    ParentResourceType = _CameraSettings.ResourceType
    parent: _CameraSettings
