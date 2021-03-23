from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionDoubleAssassinationCondition(SubclassBaseFile):
    ResourceType = 0x77B7A566
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
