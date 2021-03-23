from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ShowUIEvent(SubclassBaseFile):
    ResourceType = 0x0853D7BB
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

