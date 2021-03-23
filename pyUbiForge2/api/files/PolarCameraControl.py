from pyUbiForge2.api.game import SubclassBaseFile
from .CameraControl import CameraControl as _CameraControl


class PolarCameraControl(SubclassBaseFile):
    ResourceType = 0x4AD57894
    ParentResourceType = _CameraControl.ResourceType
    parent: _CameraControl

