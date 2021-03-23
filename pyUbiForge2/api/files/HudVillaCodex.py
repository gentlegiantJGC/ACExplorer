from pyUbiForge2.api.game import SubclassBaseFile
from .HudVilla import HudVilla as _HudVilla


class HudVillaCodex(SubclassBaseFile):
    ResourceType = 0x8DB259AC
    ParentResourceType = _HudVilla.ResourceType
    parent: _HudVilla

