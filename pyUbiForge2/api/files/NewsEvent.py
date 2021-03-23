from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class NewsEvent(SubclassBaseFile):
    ResourceType = 0xF0662190
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
