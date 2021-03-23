from pyUbiForge2.api.game import SubclassBaseFile
from .HudVilla import HudVilla as _HudVilla


class HudVillaEquipment(SubclassBaseFile):
    ResourceType = 0xB718CC73
    ParentResourceType = _HudVilla.ResourceType
    parent: _HudVilla
