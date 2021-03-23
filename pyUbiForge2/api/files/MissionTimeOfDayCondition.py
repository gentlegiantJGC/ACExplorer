from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionTimeOfDayCondition(SubclassBaseFile):
    ResourceType = 0x7861BC1D
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition
