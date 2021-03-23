from pyUbiForge2.api.game import SubclassBaseFile
from .HudVilla import HudVilla as _HudVilla


class HudVillaTrophy(SubclassBaseFile):
    ResourceType = 0x25BBEE54
    ParentResourceType = _HudVilla.ResourceType
    parent: _HudVilla

