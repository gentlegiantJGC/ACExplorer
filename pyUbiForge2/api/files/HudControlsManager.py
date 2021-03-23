from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudControlsManager(SubclassBaseFile):
    ResourceType = 0xD3E42737
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

