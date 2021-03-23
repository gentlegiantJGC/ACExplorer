from pyUbiForge2.api.game import SubclassBaseFile
from .FireItem import FireItem as _FireItem


class HudItem(SubclassBaseFile):
    ResourceType = 0x43B8FCA3
    ParentResourceType = _FireItem.ResourceType
    parent: _FireItem

