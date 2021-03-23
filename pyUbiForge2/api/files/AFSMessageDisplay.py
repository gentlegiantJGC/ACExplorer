from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class AFSMessageDisplay(SubclassBaseFile):
    ResourceType = 0xE0A37EF3
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

