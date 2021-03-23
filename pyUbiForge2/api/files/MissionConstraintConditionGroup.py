from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionConstraintConditionGroup(SubclassBaseFile):
    ResourceType = 0xA8D51E5D
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
