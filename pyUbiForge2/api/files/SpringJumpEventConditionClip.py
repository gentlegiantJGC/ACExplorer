from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class SpringJumpEventConditionClip(SubclassBaseFile):
    ResourceType = 0x27ECDF63
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
