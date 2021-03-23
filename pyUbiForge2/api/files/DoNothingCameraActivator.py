from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class DoNothingCameraActivator(SubclassBaseFile):
    ResourceType = 0x489987F1
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

