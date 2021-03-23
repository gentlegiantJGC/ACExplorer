from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepGroupOperator import (
    MissionStepGroupOperator as _MissionStepGroupOperator,
)


class MissionStepGroupOperatorAll(SubclassBaseFile):
    ResourceType = 0xDF182DA6
    ParentResourceType = _MissionStepGroupOperator.ResourceType
    parent: _MissionStepGroupOperator
