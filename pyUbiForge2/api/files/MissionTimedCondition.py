from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionTimedCondition(SubclassBaseFile):
    ResourceType = 0x19D26865
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
