from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarker import MapMarker as _MapMarker


class PlayerMapMarker(SubclassBaseFile):
    ResourceType = 0xAD8E3E85
    ParentResourceType = _MapMarker.ResourceType
    parent: _MapMarker

