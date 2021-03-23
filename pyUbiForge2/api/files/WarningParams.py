from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import (
    PushExclusiveReactionParams as _PushExclusiveReactionParams,
)


class WarningParams(SubclassBaseFile):
    ResourceType = 0xE30AD546
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams
