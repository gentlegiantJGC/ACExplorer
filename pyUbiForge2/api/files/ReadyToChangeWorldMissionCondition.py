from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class ReadyToChangeWorldMissionCondition(SubclassBaseFile):
    ResourceType = 0xE9B03D18
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition
