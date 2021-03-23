from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepGroupOperator import (
    MissionStepGroupOperator as _MissionStepGroupOperator,
)


class MissionStepGroupOperatorCount(SubclassBaseFile):
    ResourceType = 0x2BCF1D80
    ParentResourceType = _MissionStepGroupOperator.ResourceType
    parent: _MissionStepGroupOperator
