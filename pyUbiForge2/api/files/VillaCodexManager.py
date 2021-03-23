from pyUbiForge2.api.game import SubclassBaseFile
from .VillaItemsManager import VillaItemsManager as _VillaItemsManager


class VillaCodexManager(SubclassBaseFile):
    ResourceType = 0x2F19E6DC
    ParentResourceType = _VillaItemsManager.ResourceType
    parent: _VillaItemsManager
