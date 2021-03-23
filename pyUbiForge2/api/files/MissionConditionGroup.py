from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionConditionGroup(SubclassBaseFile):
    ResourceType = 0x67405E69
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

