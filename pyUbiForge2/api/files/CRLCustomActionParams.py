from pyUbiForge2.api.game import SubclassBaseFile
from .PushConcurrentReactionParams import (
    PushConcurrentReactionParams as _PushConcurrentReactionParams,
)


class CRLCustomActionParams(SubclassBaseFile):
    ResourceType = 0xD3B30B3D
    ParentResourceType = _PushConcurrentReactionParams.ResourceType
    parent: _PushConcurrentReactionParams
