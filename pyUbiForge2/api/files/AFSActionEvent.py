from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class AFSActionEvent(SubclassBaseFile):
    ResourceType = 0x67307947
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
