from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionLanguageCondition(SubclassBaseFile):
    ResourceType = 0x391FFA15
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

