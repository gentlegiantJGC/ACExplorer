from pyUbiForge2.api.game import SubclassBaseFile
from .InventoryItemContainer import InventoryItemContainer as _InventoryItemContainer


class InventoryRechargeableContainer(SubclassBaseFile):
    ResourceType = 0x08CE3886
    ParentResourceType = _InventoryItemContainer.ResourceType
    parent: _InventoryItemContainer
