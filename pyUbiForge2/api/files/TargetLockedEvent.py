from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class TargetLockedEvent(SubclassBaseFile):
    ResourceType = 0x76F48216
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

