from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class PlayerVanishedUIEvent(SubclassBaseFile):
    ResourceType = 0x2EB66767
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
