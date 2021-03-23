from pyUbiForge2.api.game import SubclassBaseFile
from .EntityDataItem import EntityDataItem as _EntityDataItem


class NPCDataItem(SubclassBaseFile):
    ResourceType = 0x9B28F5DF
    ParentResourceType = _EntityDataItem.ResourceType
    parent: _EntityDataItem
