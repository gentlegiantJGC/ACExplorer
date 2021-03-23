from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepGroupOperator import (
    MissionStepGroupOperator as _MissionStepGroupOperator,
)


class MissionStepGroupOperatorAny(SubclassBaseFile):
    ResourceType = 0x80F3ABCF
    ParentResourceType = _MissionStepGroupOperator.ResourceType
    parent: _MissionStepGroupOperator
