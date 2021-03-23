from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class AFSHidingEvent(SubclassBaseFile):
    ResourceType = 0x26E7CF06
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

