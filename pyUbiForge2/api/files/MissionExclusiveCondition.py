from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionExclusiveCondition(SubclassBaseFile):
    ResourceType = 0x939F04C0
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

