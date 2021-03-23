from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionConstraintPropertyOverride(SubclassBaseFile):
    ResourceType = 0xC5C66E28
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

