from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConditionOperator import (
    MissionConditionOperator as _MissionConditionOperator,
)


class MissionConditionOperatorAll(SubclassBaseFile):
    ResourceType = 0x991107F5
    ParentResourceType = _MissionConditionOperator.ResourceType
    parent: _MissionConditionOperator
