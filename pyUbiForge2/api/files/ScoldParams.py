from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import PushExclusiveReactionParams as _PushExclusiveReactionParams


class ScoldParams(SubclassBaseFile):
    ResourceType = 0xF2CC8CAB
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams

