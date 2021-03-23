from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MiniMapEvent(SubclassBaseFile):
    ResourceType = 0x695894E2
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
