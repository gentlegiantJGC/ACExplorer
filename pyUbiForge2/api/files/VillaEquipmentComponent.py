from pyUbiForge2.api.game import SubclassBaseFile
from .VillaInventoryItemComponent import (
    VillaInventoryItemComponent as _VillaInventoryItemComponent,
)


class VillaEquipmentComponent(SubclassBaseFile):
    ResourceType = 0x8C471D3F
    ParentResourceType = _VillaInventoryItemComponent.ResourceType
    parent: _VillaInventoryItemComponent
