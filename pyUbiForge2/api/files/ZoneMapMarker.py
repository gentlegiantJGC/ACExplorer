from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarker import MapMarker as _MapMarker


class ZoneMapMarker(SubclassBaseFile):
    ResourceType = 0xB85E8693
    ParentResourceType = _MapMarker.ResourceType
    parent: _MapMarker
