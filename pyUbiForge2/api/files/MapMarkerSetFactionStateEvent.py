from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerEvent import MapMarkerEvent as _MapMarkerEvent


class MapMarkerSetFactionStateEvent(SubclassBaseFile):
    ResourceType = 0xAB67F648
    ParentResourceType = _MapMarkerEvent.ResourceType
    parent: _MapMarkerEvent

