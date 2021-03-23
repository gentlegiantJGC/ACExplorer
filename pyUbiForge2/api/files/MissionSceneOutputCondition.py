from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import MissionConstraintCondition as _MissionConstraintCondition


class MissionSceneOutputCondition(SubclassBaseFile):
    ResourceType = 0x6087DF35
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition

