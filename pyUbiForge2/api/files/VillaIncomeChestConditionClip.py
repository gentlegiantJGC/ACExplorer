from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class VillaIncomeChestConditionClip(SubclassBaseFile):
    ResourceType = 0xCA626C9B
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
