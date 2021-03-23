from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class EnterShopMenuEvent(SubclassBaseFile):
    ResourceType = 0xDEC49798
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

