from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class InventoryItemContainer(SubclassBaseFile):
    ResourceType = 0x6D8B7591
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

