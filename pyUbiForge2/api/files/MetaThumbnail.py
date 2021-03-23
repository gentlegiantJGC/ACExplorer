from pyUbiForge2.api.game import SubclassBaseFile
from .MetaDataItem import MetaDataItem as _MetaDataItem


class MetaThumbnail(SubclassBaseFile):
    ResourceType = 0x9255529B
    ParentResourceType = _MetaDataItem.ResourceType
    parent: _MetaDataItem
