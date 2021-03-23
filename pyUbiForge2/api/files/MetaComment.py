from pyUbiForge2.api.game import SubclassBaseFile
from .MetaDataItem import MetaDataItem as _MetaDataItem


class MetaComment(SubclassBaseFile):
    ResourceType = 0x363EAC42
    ParentResourceType = _MetaDataItem.ResourceType
    parent: _MetaDataItem
