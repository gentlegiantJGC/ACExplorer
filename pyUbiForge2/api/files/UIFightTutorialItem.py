from pyUbiForge2.api.game import SubclassBaseFile
from .UIInventoryItem import UIInventoryItem as _UIInventoryItem


class UIFightTutorialItem(SubclassBaseFile):
    ResourceType = 0xC7D41F2A
    ParentResourceType = _UIInventoryItem.ResourceType
    parent: _UIInventoryItem

