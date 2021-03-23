from pyUbiForge2.api.game import SubclassBaseFile
from .MissionTimedCondition import MissionTimedCondition as _MissionTimedCondition


class MissionDisplayedTimerCondition(SubclassBaseFile):
    ResourceType = 0xE8FCEC38
    ParentResourceType = _MissionTimedCondition.ResourceType
    parent: _MissionTimedCondition
