from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConditionOperator import (
    MissionConditionOperator as _MissionConditionOperator,
)


class MissionConditionOperatorAny(SubclassBaseFile):
    ResourceType = 0xC6FA819C
    ParentResourceType = _MissionConditionOperator.ResourceType
    parent: _MissionConditionOperator
