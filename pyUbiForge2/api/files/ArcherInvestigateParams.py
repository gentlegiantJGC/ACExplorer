from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import PushExclusiveReactionParams as _PushExclusiveReactionParams


class ArcherInvestigateParams(SubclassBaseFile):
    ResourceType = 0xA82A6A8E
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams

