from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionPlayerInOddZoneCondition(SubclassBaseFile):
    ResourceType = 0xB9D7EF35
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
