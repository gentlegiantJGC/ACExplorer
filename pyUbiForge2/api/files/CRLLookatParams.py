from pyUbiForge2.api.game import SubclassBaseFile
from .PushConcurrentReactionParams import PushConcurrentReactionParams as _PushConcurrentReactionParams


class CRLLookatParams(SubclassBaseFile):
    ResourceType = 0xD85E13F3
    ParentResourceType = _PushConcurrentReactionParams.ResourceType
    parent: _PushConcurrentReactionParams

