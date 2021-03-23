from pyUbiForge2.api.game import SubclassBaseFile
from .MetaDataItem import MetaDataItem as _MetaDataItem


class MetaCategories(SubclassBaseFile):
    ResourceType = 0x1416499D
    ParentResourceType = _MetaDataItem.ResourceType
    parent: _MetaDataItem

