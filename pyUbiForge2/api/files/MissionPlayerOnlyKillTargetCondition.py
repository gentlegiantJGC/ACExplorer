from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionPlayerOnlyKillTargetCondition(SubclassBaseFile):
    ResourceType = 0x3338F2BF
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

