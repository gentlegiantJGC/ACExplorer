from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerEvent import MapMarkerEvent as _MapMarkerEvent


class MapMarkerRevertToKeyEntityEvent(SubclassBaseFile):
    ResourceType = 0x272BD565
    ParentResourceType = _MapMarkerEvent.ResourceType
    parent: _MapMarkerEvent

