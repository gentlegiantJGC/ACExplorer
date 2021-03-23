from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NavigationDudeEvent(SubclassBaseFile):
    ResourceType = 0x5B446C0C
    ParentResourceType = _Event.ResourceType
    parent: _Event

