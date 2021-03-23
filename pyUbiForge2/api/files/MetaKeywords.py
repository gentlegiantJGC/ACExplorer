from pyUbiForge2.api.game import SubclassBaseFile
from .MetaDataItem import MetaDataItem as _MetaDataItem


class MetaKeywords(SubclassBaseFile):
    ResourceType = 0x762BF26F
    ParentResourceType = _MetaDataItem.ResourceType
    parent: _MetaDataItem
