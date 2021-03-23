from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionPSPConnectionDoneCondition(SubclassBaseFile):
    ResourceType = 0xAB8638B6
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

