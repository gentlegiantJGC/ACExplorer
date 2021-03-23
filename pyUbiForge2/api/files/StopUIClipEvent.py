from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class StopUIClipEvent(SubclassBaseFile):
    ResourceType = 0x94613E1E
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
