from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class PlayerSeenEvent(SubclassBaseFile):
    ResourceType = 0x4232220A
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
