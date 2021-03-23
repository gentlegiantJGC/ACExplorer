from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudVilla(SubclassBaseFile):
    ResourceType = 0xF1227132
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

