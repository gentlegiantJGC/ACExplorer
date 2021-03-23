from pyUbiForge2.api.game import SubclassBaseFile
from .ActionMapMarker import ActionMapMarker as _ActionMapMarker


class ActionDLCMapMarker(SubclassBaseFile):
    ResourceType = 0x7213EE54
    ParentResourceType = _ActionMapMarker.ResourceType
    parent: _ActionMapMarker

