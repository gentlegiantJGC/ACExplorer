from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudIconManager(SubclassBaseFile):
    ResourceType = 0x564FAF5E
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

