from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionKillTargetWeaponCondition(SubclassBaseFile):
    ResourceType = 0x9F74C6CC
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
