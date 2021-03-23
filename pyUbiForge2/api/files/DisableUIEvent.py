from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class DisableUIEvent(SubclassBaseFile):
    ResourceType = 0x50FF8C4F
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
