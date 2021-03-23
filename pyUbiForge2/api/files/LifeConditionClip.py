from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class LifeConditionClip(SubclassBaseFile):
    ResourceType = 0x381CA979
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
