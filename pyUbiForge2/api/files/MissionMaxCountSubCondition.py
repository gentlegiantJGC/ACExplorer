from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionMaxCountSubCondition(SubclassBaseFile):
    ResourceType = 0x3F96A250
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

