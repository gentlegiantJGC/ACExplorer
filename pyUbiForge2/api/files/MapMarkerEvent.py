from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MapMarkerEvent(SubclassBaseFile):
    ResourceType = 0x03D30D6C
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

