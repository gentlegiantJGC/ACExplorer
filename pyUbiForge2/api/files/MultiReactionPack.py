from pyUbiForge2.api.game import SubclassBaseFile
from .ReactionPack import ReactionPack as _ReactionPack


class MultiReactionPack(SubclassBaseFile):
    ResourceType = 0x0B72B983
    ParentResourceType = _ReactionPack.ResourceType
    parent: _ReactionPack

