from pyUbiForge2.api.game import SubclassBaseFile
from .CameraActivator import CameraActivator as _CameraActivator


class FightSpecialMovesCameraActivator(SubclassBaseFile):
    ResourceType = 0x5A06215E
    ParentResourceType = _CameraActivator.ResourceType
    parent: _CameraActivator

