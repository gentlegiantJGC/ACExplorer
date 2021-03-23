from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIMissionFailedEvent(SubclassBaseFile):
    ResourceType = 0x1341E87F
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
