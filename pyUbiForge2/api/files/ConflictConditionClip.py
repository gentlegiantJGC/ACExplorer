from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class ConflictConditionClip(SubclassBaseFile):
    ResourceType = 0x9C4C7B75
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
