from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class MissionExclusiveConditionClip(SubclassBaseFile):
    ResourceType = 0xE389A9A8
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

