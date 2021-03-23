from pyUbiForge2.api.game import SubclassBaseFile
from .MetaDataItem import MetaDataItem as _MetaDataItem


class MetaProductionStatus(SubclassBaseFile):
    ResourceType = 0xF8E88D1B
    ParentResourceType = _MetaDataItem.ResourceType
    parent: _MetaDataItem
