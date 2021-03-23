from pyUbiForge2.api.game import SubclassBaseFile
from .HudVilla import HudVilla as _HudVilla


class HudVillaWorkshop(SubclassBaseFile):
    ResourceType = 0xD0DE32DD
    ParentResourceType = _HudVilla.ResourceType
    parent: _HudVilla
