from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ShowChangeWorldGateMenuEvent(SubclassBaseFile):
    ResourceType = 0x7F30E564
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

