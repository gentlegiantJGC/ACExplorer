from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import (
    PushExclusiveReactionParams as _PushExclusiveReactionParams,
)


class GrabMoneyParams(SubclassBaseFile):
    ResourceType = 0xEBEE3146
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams
