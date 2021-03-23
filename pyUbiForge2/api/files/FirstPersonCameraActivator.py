from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class FirstPersonCameraActivator(SubclassBaseFile):
    ResourceType = 0xA66B4B0C
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

