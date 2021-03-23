from pyUbiForge2.api.game import SubclassBaseFile
from .VillaItemsManager import VillaItemsManager as _VillaItemsManager


class VillaVaultManager(SubclassBaseFile):
    ResourceType = 0xDAB41EF4
    ParentResourceType = _VillaItemsManager.ResourceType
    parent: _VillaItemsManager
