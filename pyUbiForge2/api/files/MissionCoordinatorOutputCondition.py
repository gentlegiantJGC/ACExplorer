from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionCoordinatorOutputCondition(SubclassBaseFile):
    ResourceType = 0x7A5F1560
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
