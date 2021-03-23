from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class InventoryMenu(SubclassBaseFile):
    ResourceType = 0x5A48A8C6
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
