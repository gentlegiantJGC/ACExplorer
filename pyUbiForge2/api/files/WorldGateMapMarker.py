from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarker import MapMarker as _MapMarker


class WorldGateMapMarker(SubclassBaseFile):
    ResourceType = 0x8C69BE21
    ParentResourceType = _MapMarker.ResourceType
    parent: _MapMarker
