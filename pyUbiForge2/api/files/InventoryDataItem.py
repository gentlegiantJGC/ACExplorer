from pyUbiForge2.api.game import SubclassBaseFile
from .EntityDataItem import EntityDataItem as _EntityDataItem


class InventoryDataItem(SubclassBaseFile):
    ResourceType = 0x54576542
    ParentResourceType = _EntityDataItem.ResourceType
    parent: _EntityDataItem

