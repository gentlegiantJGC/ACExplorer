from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import (
    PushExclusiveReactionParams as _PushExclusiveReactionParams,
)


class FleeParams(SubclassBaseFile):
    ResourceType = 0xB25C0ADA
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams
