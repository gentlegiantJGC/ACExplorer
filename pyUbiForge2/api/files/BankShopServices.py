from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractShopServices import AbstractShopServices as _AbstractShopServices


class BankShopServices(SubclassBaseFile):
    ResourceType = 0x8E07866C
    ParentResourceType = _AbstractShopServices.ResourceType
    parent: _AbstractShopServices
