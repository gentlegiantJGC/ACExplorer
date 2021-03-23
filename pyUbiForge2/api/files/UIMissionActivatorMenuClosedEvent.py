from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIMissionActivatorMenuClosedEvent(SubclassBaseFile):
    ResourceType = 0xF4E66A5D
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
