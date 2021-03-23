from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudWeaponSelect(SubclassBaseFile):
    ResourceType = 0xFA1F3765
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

