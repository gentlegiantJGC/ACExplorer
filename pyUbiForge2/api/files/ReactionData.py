from pyUbiForge2.api.game import SubclassBaseFile
from .BaseReactionData import BaseReactionData as _BaseReactionData


class ReactionData(SubclassBaseFile):
    ResourceType = 0x14CC8B17
    ParentResourceType = _BaseReactionData.ResourceType
    parent: _BaseReactionData
