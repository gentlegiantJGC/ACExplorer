from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ConflictStateChangedUIEvent(SubclassBaseFile):
    ResourceType = 0xE6B18123
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

