from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionPlayerNotorietyCondition(SubclassBaseFile):
    ResourceType = 0x155705C1
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

