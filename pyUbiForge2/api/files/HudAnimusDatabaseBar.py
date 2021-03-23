from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudAnimusDatabaseBar(SubclassBaseFile):
    ResourceType = 0x00D4029F
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

