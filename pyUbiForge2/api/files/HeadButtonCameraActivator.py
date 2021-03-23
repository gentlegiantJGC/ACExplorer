from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class HeadButtonCameraActivator(SubclassBaseFile):
    ResourceType = 0x369D719C
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

