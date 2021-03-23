from pyUbiForge2.api.game import SubclassBaseFile
from .HudVillaEquipment import HudVillaEquipment as _HudVillaEquipment


class HudVillaArmor(SubclassBaseFile):
    ResourceType = 0x40EABF95
    ParentResourceType = _HudVillaEquipment.ResourceType
    parent: _HudVillaEquipment
