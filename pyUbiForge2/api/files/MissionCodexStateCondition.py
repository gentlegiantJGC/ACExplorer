from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionCodexStateCondition(SubclassBaseFile):
    ResourceType = 0x4CA9DD38
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

