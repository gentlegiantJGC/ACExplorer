from pyUbiForge2.api.game import SubclassBaseFile
from .HudItem import HudItem as _HudItem


class HudMissionState(SubclassBaseFile):
    ResourceType = 0x07F6E581
    ParentResourceType = _HudItem.ResourceType
    parent: _HudItem
