from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class VillaBuildingTriggerConditionClip(SubclassBaseFile):
    ResourceType = 0x54D7055D
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

