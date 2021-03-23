from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionUniqueKeyUnlockedCondition(SubclassBaseFile):
    ResourceType = 0x74A18E50
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

