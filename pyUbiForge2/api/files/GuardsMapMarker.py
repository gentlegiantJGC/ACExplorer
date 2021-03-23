from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarker import MapMarker as _MapMarker


class GuardsMapMarker(SubclassBaseFile):
    ResourceType = 0xE5D77D0C
    ParentResourceType = _MapMarker.ResourceType
    parent: _MapMarker
