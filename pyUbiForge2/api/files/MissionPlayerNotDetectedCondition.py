from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionPlayerNotDetectedCondition(SubclassBaseFile):
    ResourceType = 0x3846BFF4
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

