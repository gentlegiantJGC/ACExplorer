from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionGroupStateCondition(SubclassBaseFile):
    ResourceType = 0xE4EDA52A
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

