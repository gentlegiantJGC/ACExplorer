from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class IsLoadingConditionClip(SubclassBaseFile):
    ResourceType = 0x4E3CEAF5
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
