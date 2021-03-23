from pyUbiForge2.api.game import SubclassBaseFile
from .VillaBuildingLevelSettings import VillaBuildingLevelSettings as _VillaBuildingLevelSettings


class VillaShopLevelSettings(SubclassBaseFile):
    ResourceType = 0xC551D243
    ParentResourceType = _VillaBuildingLevelSettings.ResourceType
    parent: _VillaBuildingLevelSettings

