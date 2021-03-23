from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionVillaTriggerCondition(SubclassBaseFile):
    ResourceType = 0xFCCDCD7D
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

