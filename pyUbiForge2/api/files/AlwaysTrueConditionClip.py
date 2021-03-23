from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class AlwaysTrueConditionClip(SubclassBaseFile):
    ResourceType = 0x2C51FF91
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

