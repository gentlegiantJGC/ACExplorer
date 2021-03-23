from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class AC2FightAdjustmentModifier(SubclassBaseFile):
    ResourceType = 0xF4CC13E4
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

