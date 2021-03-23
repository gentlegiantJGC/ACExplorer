from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class ActingInterruptConditionClip(SubclassBaseFile):
    ResourceType = 0x5AD11BD1
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

