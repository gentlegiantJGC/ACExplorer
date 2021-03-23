from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionPlayerUseLeapOfFaithCondition(SubclassBaseFile):
    ResourceType = 0x88488F76
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

