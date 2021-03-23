from pyUbiForge2.api.game import SubclassBaseFile
from .HudVilla import HudVilla as _HudVilla


class HudVillaSummary(SubclassBaseFile):
    ResourceType = 0x7BCC3846
    ParentResourceType = _HudVilla.ResourceType
    parent: _HudVilla

