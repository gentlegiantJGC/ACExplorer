from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class FightCameraActivator(SubclassBaseFile):
    ResourceType = 0x6258E6C1
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator
