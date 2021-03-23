from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ShopItemSettings(SubclassBaseFile):
    ResourceType = 0xE0E2E1D1
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

