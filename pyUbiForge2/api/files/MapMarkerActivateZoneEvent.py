from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerActivateEvent import MapMarkerActivateEvent as _MapMarkerActivateEvent


class MapMarkerActivateZoneEvent(SubclassBaseFile):
    ResourceType = 0x9C44F137
    ParentResourceType = _MapMarkerActivateEvent.ResourceType
    parent: _MapMarkerActivateEvent

