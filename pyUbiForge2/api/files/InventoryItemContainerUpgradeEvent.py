from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class InventoryItemContainerUpgradeEvent(SubclassBaseFile):
    ResourceType = 0x004B6D99
    ParentResourceType = _Event.ResourceType
    parent: _Event

