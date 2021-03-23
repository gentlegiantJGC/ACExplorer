from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NavigationErrorEvent(SubclassBaseFile):
    ResourceType = 0x18AA2BF2
    ParentResourceType = _Event.ResourceType
    parent: _Event

