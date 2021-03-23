from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionPlayerAvoidZonesCondition(SubclassBaseFile):
    ResourceType = 0xC65F012F
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
