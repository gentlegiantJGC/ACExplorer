from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractShopServices import AbstractShopServices as _AbstractShopServices


class FastTravelShopServices(SubclassBaseFile):
    ResourceType = 0x83C593AA
    ParentResourceType = _AbstractShopServices.ResourceType
    parent: _AbstractShopServices
