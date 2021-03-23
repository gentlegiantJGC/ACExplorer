from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class PlayerWealthEvent(SubclassBaseFile):
    ResourceType = 0x13107B62
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

