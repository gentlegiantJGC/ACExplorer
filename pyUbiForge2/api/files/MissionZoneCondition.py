from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionZoneCondition(SubclassBaseFile):
    ResourceType = 0x1DE8F7EE
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
