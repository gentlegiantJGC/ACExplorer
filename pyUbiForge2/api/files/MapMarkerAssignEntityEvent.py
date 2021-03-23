from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerEvent import MapMarkerEvent as _MapMarkerEvent


class MapMarkerAssignEntityEvent(SubclassBaseFile):
    ResourceType = 0xD0851E60
    ParentResourceType = _MapMarkerEvent.ResourceType
    parent: _MapMarkerEvent

