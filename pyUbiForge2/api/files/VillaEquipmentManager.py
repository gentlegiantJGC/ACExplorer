from pyUbiForge2.api.game import SubclassBaseFile
from .VillaItemsManager import VillaItemsManager as _VillaItemsManager


class VillaEquipmentManager(SubclassBaseFile):
    ResourceType = 0xCB10913B
    ParentResourceType = _VillaItemsManager.ResourceType
    parent: _VillaItemsManager
