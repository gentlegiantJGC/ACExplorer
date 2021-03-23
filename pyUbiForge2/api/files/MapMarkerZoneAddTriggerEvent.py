from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerEvent import MapMarkerEvent as _MapMarkerEvent


class MapMarkerZoneAddTriggerEvent(SubclassBaseFile):
    ResourceType = 0xBA8C0294
    ParentResourceType = _MapMarkerEvent.ResourceType
    parent: _MapMarkerEvent

