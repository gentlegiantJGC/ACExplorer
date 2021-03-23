from pyUbiForge2.api.game import SubclassBaseFile
from .MapMarkerComponent import MapMarkerComponent as _MapMarkerComponent


class WorldGateMapMarkerComponent(SubclassBaseFile):
    ResourceType = 0xEAA5AC14
    ParentResourceType = _MapMarkerComponent.ResourceType
    parent: _MapMarkerComponent

