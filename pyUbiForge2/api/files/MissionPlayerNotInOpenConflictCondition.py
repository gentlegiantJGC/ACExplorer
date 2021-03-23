from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionPlayerNotInOpenConflictCondition(SubclassBaseFile):
    ResourceType = 0x24AB5D3C
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

