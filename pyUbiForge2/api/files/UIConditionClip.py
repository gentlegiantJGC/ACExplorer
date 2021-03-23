from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class UIConditionClip(SubclassBaseFile):
    ResourceType = 0x300FF782
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
