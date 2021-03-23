from pyUbiForge2.api.game import SubclassBaseFile
from .ProximityEvent import ProximityEvent as _ProximityEvent


class ProximityPerceptionEvent(SubclassBaseFile):
    ResourceType = 0xC650220C
    ParentResourceType = _ProximityEvent.ResourceType
    parent: _ProximityEvent

