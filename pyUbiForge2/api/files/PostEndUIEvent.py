from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class PostEndUIEvent(SubclassBaseFile):
    ResourceType = 0x1F78B8DD
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

