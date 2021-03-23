from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class EndCreditsEvent(SubclassBaseFile):
    ResourceType = 0x1629DFA7
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
