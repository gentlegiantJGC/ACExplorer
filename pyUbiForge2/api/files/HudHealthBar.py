from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudHealthBar(SubclassBaseFile):
    ResourceType = 0xF64650D1
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

