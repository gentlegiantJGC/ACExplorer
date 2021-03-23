from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class AssassinationConditionClip(SubclassBaseFile):
    ResourceType = 0x3FF7C7B6
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
