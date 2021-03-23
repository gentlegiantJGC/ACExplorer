from pyUbiForge2.api.game import SubclassBaseFile
from .PushConcurrentReactionParams import (
    PushConcurrentReactionParams as _PushConcurrentReactionParams,
)


class CRLDetectParams(SubclassBaseFile):
    ResourceType = 0x69549B79
    ParentResourceType = _PushConcurrentReactionParams.ResourceType
    parent: _PushConcurrentReactionParams
