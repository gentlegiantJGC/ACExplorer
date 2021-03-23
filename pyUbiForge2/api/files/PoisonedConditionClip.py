from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class PoisonedConditionClip(SubclassBaseFile):
    ResourceType = 0xC6FA16A1
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

