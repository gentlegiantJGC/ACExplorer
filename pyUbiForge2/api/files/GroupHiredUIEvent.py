from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class GroupHiredUIEvent(SubclassBaseFile):
    ResourceType = 0xE69B401C
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

