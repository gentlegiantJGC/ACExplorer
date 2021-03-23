from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class UPlayConditionClip(SubclassBaseFile):
    ResourceType = 0xC96A5477
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
