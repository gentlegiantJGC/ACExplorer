from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ExitShopMenuEvent(SubclassBaseFile):
    ResourceType = 0xAF7BAF95
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

