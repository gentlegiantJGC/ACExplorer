from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionVillaBuildingTriggerCondition(SubclassBaseFile):
    ResourceType = 0x1196817C
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition
