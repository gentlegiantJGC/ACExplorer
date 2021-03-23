from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIMissionTransitionEvent(SubclassBaseFile):
    ResourceType = 0x2339121E
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
