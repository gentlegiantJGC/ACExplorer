from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class TargetSetEvent(SubclassBaseFile):
    ResourceType = 0xB9BFF5A9
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
