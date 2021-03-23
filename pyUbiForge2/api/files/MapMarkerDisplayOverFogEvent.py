from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MapMarkerDisplayOverFogEvent(SubclassBaseFile):
    ResourceType = 0x5A92DD5F
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

