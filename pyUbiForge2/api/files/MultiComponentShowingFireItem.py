from pyUbiForge2.api.game import SubclassBaseFile
from .FireItem import FireItem as _FireItem


class MultiComponentShowingFireItem(SubclassBaseFile):
    ResourceType = 0xA8958C7C
    ParentResourceType = _FireItem.ResourceType
    parent: _FireItem
