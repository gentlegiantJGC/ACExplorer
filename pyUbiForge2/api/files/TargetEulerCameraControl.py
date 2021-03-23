from pyUbiForge2.api.game import SubclassBaseFile
from .CameraControl import CameraControl as _CameraControl


class TargetEulerCameraControl(SubclassBaseFile):
    ResourceType = 0x1D2AD788
    ParentResourceType = _CameraControl.ResourceType
    parent: _CameraControl
