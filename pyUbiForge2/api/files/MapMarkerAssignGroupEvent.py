from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerEvent import MapMarkerEvent as _MapMarkerEvent


class MapMarkerAssignGroupEvent(SubclassBaseFile):
    ResourceType = 0x38E4206E
    ParentResourceType = _MapMarkerEvent.ResourceType
    parent: _MapMarkerEvent
