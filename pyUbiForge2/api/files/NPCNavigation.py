from pyUbiForge2.api.game import SubclassBaseFile
from .Pattern import Pattern as _Pattern


class NPCNavigation(SubclassBaseFile):
    ResourceType = 0xDE2350E2
    ParentResourceType = _Pattern.ResourceType
    parent: _Pattern

