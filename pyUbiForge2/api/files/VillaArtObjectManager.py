from pyUbiForge2.api.game import SubclassBaseFile
from .VillaItemsManager import VillaItemsManager as _VillaItemsManager


class VillaArtObjectManager(SubclassBaseFile):
    ResourceType = 0xB89F432C
    ParentResourceType = _VillaItemsManager.ResourceType
    parent: _VillaItemsManager

