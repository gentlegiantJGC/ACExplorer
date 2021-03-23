from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionGroupWaitCondition(SubclassBaseFile):
    ResourceType = 0x355F08D9
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
