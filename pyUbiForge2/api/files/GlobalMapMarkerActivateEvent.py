from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class GlobalMapMarkerActivateEvent(SubclassBaseFile):
    ResourceType = 0x383A0927
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
