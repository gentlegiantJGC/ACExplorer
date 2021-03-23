from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class HorseRidingConditionClip(SubclassBaseFile):
    ResourceType = 0x9685040E
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
