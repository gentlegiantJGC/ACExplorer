from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class FightModifier(SubclassBaseFile):
    ResourceType = 0x869C6F49
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

