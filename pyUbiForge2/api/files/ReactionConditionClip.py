from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class ReactionConditionClip(SubclassBaseFile):
    ResourceType = 0xB83324E0
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
