from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIFXEvent(SubclassBaseFile):
    ResourceType = 0x1355D136
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
