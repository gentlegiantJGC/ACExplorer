from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import PushExclusiveReactionParams as _PushExclusiveReactionParams


class LowMoraleFleeParams(SubclassBaseFile):
    ResourceType = 0x96B0D491
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams

