from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class AssassinButtonPressedCameraActivator(SubclassBaseFile):
    ResourceType = 0x3EE2A80A
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

