from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import (
    PushExclusiveReactionParams as _PushExclusiveReactionParams,
)


class BeatUpParams(SubclassBaseFile):
    ResourceType = 0xDD6AAF02
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams
