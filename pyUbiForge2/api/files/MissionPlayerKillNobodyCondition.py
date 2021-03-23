from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionPlayerKillNobodyCondition(SubclassBaseFile):
    ResourceType = 0x80CF6EF0
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
