from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarker import MapMarker as _MapMarker


class VillaMapMarker(SubclassBaseFile):
    ResourceType = 0x25F27357
    ParentResourceType = _MapMarker.ResourceType
    parent: _MapMarker
