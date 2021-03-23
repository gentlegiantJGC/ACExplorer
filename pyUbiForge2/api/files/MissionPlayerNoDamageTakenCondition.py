from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionPlayerNoDamageTakenCondition(SubclassBaseFile):
    ResourceType = 0x052891FF
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

