from pyUbiForge2.api.game import SubclassBaseFile
from .BaseReactionPack import BaseReactionPack as _BaseReactionPack


class ReactionPack(SubclassBaseFile):
    ResourceType = 0x2EE12657
    ParentResourceType = _BaseReactionPack.ResourceType
    parent: _BaseReactionPack

