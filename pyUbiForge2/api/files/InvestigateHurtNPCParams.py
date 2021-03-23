from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import (
    PushExclusiveReactionParams as _PushExclusiveReactionParams,
)


class InvestigateHurtNPCParams(SubclassBaseFile):
    ResourceType = 0xE80F9451
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams
