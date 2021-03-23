from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConditionOperator import (
    MissionConditionOperator as _MissionConditionOperator,
)


class MissionConditionOperatorCount(SubclassBaseFile):
    ResourceType = 0x61E29CC8
    ParentResourceType = _MissionConditionOperator.ResourceType
    parent: _MissionConditionOperator
