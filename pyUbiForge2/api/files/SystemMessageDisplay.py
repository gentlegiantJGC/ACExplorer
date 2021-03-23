from pyUbiForge2.api.game import SubclassBaseFile
from .FireItem import FireItem as _FireItem


class SystemMessageDisplay(SubclassBaseFile):
    ResourceType = 0x0B1216DB
    ParentResourceType = _FireItem.ResourceType
    parent: _FireItem

