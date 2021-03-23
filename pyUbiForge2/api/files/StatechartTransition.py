from pyUbiForge2.api.game import SubclassBaseFile
from .StatechartReaction import StatechartReaction as _StatechartReaction


class StatechartTransition(SubclassBaseFile):
    ResourceType = 0x5A33F984
    ParentResourceType = _StatechartReaction.ResourceType
    parent: _StatechartReaction
