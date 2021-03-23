from pyUbiForge2.api.game import SubclassBaseFile
from .PushConcurrentReactionParams import (
    PushConcurrentReactionParams as _PushConcurrentReactionParams,
)


class CRLDetectNPCParams(SubclassBaseFile):
    ResourceType = 0x9B83E269
    ParentResourceType = _PushConcurrentReactionParams.ResourceType
    parent: _PushConcurrentReactionParams
