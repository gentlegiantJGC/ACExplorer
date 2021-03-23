from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractShopServices import AbstractShopServices as _AbstractShopServices


class BlacksmithShopServices(SubclassBaseFile):
    ResourceType = 0x8A315084
    ParentResourceType = _AbstractShopServices.ResourceType
    parent: _AbstractShopServices

