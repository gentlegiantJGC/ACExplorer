from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudGroupInfo(SubclassBaseFile):
    ResourceType = 0xDB79A43D
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem

