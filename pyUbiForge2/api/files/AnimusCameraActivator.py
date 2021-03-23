from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class AnimusCameraActivator(SubclassBaseFile):
    ResourceType = 0x2A06F784
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
