from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionKillTargetMethodCondition(SubclassBaseFile):
    ResourceType = 0x08073A97
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

