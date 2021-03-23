from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstractReaction import CLAbstractReaction as _CLAbstractReaction


class CLReaction(SubclassBaseFile):
    ResourceType = 0x96229E0E
    ParentResourceType = _CLAbstractReaction.ResourceType
    parent: _CLAbstractReaction
