from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class PlayerInConflictUIEvent(SubclassBaseFile):
    ResourceType = 0xCBA5E396
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
