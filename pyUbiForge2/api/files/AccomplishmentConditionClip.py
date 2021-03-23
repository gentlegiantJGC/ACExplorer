from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class AccomplishmentConditionClip(SubclassBaseFile):
    ResourceType = 0x7E1B0897
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

