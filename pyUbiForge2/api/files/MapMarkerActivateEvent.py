from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerEvent import MapMarkerEvent as _MapMarkerEvent


class MapMarkerActivateEvent(SubclassBaseFile):
    ResourceType = 0xC7F9DFC8
    ParentResourceType = _MapMarkerEvent.ResourceType
    parent: _MapMarkerEvent
