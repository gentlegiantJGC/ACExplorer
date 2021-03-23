from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionFlythroughCondition(SubclassBaseFile):
    ResourceType = 0x5F36F8E1
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition
