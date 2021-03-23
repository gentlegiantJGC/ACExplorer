from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIMissionFailedBoxClosedEvent(SubclassBaseFile):
    ResourceType = 0x9422E51C
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

