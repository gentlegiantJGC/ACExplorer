from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudMiniMap(SubclassBaseFile):
    ResourceType = 0xBED8093E
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

