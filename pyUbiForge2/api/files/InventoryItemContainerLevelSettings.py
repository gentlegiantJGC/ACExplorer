from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class InventoryItemContainerLevelSettings(SubclassBaseFile):
    ResourceType = 0x7F66DCB3
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
