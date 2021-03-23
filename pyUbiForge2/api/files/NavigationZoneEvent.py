from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NavigationZoneEvent(SubclassBaseFile):
    ResourceType = 0x764D8742
    ParentResourceType = _Event.ResourceType
    parent: _Event
