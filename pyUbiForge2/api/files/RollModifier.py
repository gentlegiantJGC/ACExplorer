from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class RollModifier(SubclassBaseFile):
    ResourceType = 0x2EDE928E
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

