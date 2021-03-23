from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import PushExclusiveReactionParams as _PushExclusiveReactionParams


class DazedParams(SubclassBaseFile):
    ResourceType = 0x88EC91CB
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams

