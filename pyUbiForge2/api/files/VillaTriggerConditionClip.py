from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class VillaTriggerConditionClip(SubclassBaseFile):
    ResourceType = 0x663D780C
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

