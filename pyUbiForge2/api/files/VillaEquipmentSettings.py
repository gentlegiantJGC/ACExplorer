from pyUbiForge2.api.game import SubclassBaseFile
from .VillaItemSettings import VillaItemSettings as _VillaItemSettings


class VillaEquipmentSettings(SubclassBaseFile):
    ResourceType = 0xE6C2767D
    ParentResourceType = _VillaItemSettings.ResourceType
    parent: _VillaItemSettings

