from pyUbiForge2.api.game import SubclassBaseFile
from .HudVillaEquipment import HudVillaEquipment as _HudVillaEquipment


class HudVillaWeapon(SubclassBaseFile):
    ResourceType = 0x5DA2B35B
    ParentResourceType = _HudVillaEquipment.ResourceType
    parent: _HudVillaEquipment

