from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionStateCondition(SubclassBaseFile):
    ResourceType = 0x0A8439B5
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

