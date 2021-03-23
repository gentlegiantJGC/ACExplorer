from pyUbiForge2.api.game import SubclassBaseFile
from .EntityDataItem import EntityDataItem as _EntityDataItem


class PlayerDataItem(SubclassBaseFile):
    ResourceType = 0x976076D9
    ParentResourceType = _EntityDataItem.ResourceType
    parent: _EntityDataItem
