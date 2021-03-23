from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class NotCameraActivator(SubclassBaseFile):
    ResourceType = 0x8B5554B5
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
