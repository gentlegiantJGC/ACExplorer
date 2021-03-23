from pyUbiForge2.api.game import SubclassBaseFile
from .VillaInventoryItemComponent import (
    VillaInventoryItemComponent as _VillaInventoryItemComponent,
)


class VillaCodexPageItemComponent(SubclassBaseFile):
    ResourceType = 0x8F4CB1BA
    ParentResourceType = _VillaInventoryItemComponent.ResourceType
    parent: _VillaInventoryItemComponent
