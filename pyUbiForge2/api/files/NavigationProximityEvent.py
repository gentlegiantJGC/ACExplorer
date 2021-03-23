from pyUbiForge2.api.game import SubclassBaseFile
from .ProximityEvent import ProximityEvent as _ProximityEvent


class NavigationProximityEvent(SubclassBaseFile):
    ResourceType = 0x25454394
    ParentResourceType = _ProximityEvent.ResourceType
    parent: _ProximityEvent

