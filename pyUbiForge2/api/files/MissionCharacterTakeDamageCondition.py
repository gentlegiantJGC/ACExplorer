from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConstraintCondition import (
    MissionConstraintCondition as _MissionConstraintCondition,
)


class MissionCharacterTakeDamageCondition(SubclassBaseFile):
    ResourceType = 0xF22E3D0B
    ParentResourceType = _MissionConstraintCondition.ResourceType
    parent: _MissionConstraintCondition
