from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class InventoryItemSettings(SubclassBaseFile):
    ResourceType = 0xC69075AB
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

