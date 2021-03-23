from pyUbiForge2.api.game import SubclassBaseFile
from .PushExclusiveReactionParams import PushExclusiveReactionParams as _PushExclusiveReactionParams


class TargetInvestigateParams(SubclassBaseFile):
    ResourceType = 0x04251D52
    ParentResourceType = _PushExclusiveReactionParams.ResourceType
    parent: _PushExclusiveReactionParams

