from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionMaxTimeSubCondition(SubclassBaseFile):
    ResourceType = 0x33C5BA97
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

