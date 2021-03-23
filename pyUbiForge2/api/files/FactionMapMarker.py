from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarker import MapMarker as _MapMarker


class FactionMapMarker(SubclassBaseFile):
    ResourceType = 0xB2CCE631
    ParentResourceType = _MapMarker.ResourceType
    parent: _MapMarker

