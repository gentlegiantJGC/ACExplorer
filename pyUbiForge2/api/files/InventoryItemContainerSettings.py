from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class InventoryItemContainerSettings(SubclassBaseFile):
    ResourceType = 0x549CDE97
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

