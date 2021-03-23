from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractMapMarkerComponent import AbstractMapMarkerComponent as _AbstractMapMarkerComponent


class MapMarkerComponent(SubclassBaseFile):
    ResourceType = 0x5F6E61F0
    ParentResourceType = _AbstractMapMarkerComponent.ResourceType
    parent: _AbstractMapMarkerComponent

