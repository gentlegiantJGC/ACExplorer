from pyUbiForge2.api.game import SubclassBaseFile
from .UIInventoryItem import UIInventoryItem as _UIInventoryItem


class UIFastTravelItem(SubclassBaseFile):
    ResourceType = 0xF2C62610
    ParentResourceType = _UIInventoryItem.ResourceType
    parent: _UIInventoryItem

