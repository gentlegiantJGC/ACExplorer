from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class HideUIEvent(SubclassBaseFile):
    ResourceType = 0xD68D5781
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
