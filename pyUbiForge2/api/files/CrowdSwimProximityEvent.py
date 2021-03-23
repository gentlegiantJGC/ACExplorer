from pyUbiForge2.api.game import SubclassBaseFile
from .ProximityEvent import ProximityEvent as _ProximityEvent


class CrowdSwimProximityEvent(SubclassBaseFile):
    ResourceType = 0x839A86A1
    ParentResourceType = _ProximityEvent.ResourceType
    parent: _ProximityEvent
