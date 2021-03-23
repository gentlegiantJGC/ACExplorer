from pyUbiForge2.api.game import SubclassBaseFile
from .EntityDataItem import EntityDataItem as _EntityDataItem


class SharedDataItem(SubclassBaseFile):
    ResourceType = 0xD743852B
    ParentResourceType = _EntityDataItem.ResourceType
    parent: _EntityDataItem
