from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class UniqueKeyUnlockedConditionClip(SubclassBaseFile):
    ResourceType = 0xC3065953
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
