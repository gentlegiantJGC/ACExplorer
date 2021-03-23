from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class ExitWhiteRoomCameraActivator(SubclassBaseFile):
    ResourceType = 0xCB8260DA
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

