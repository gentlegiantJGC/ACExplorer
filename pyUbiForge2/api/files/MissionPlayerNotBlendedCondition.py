from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionPlayerNotBlendedCondition(SubclassBaseFile):
    ResourceType = 0x7C479903
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
