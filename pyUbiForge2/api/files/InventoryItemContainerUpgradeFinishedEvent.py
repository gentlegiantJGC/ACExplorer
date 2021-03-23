from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class InventoryItemContainerUpgradeFinishedEvent(SubclassBaseFile):
    ResourceType = 0xC9610F30
    ParentResourceType = _Event.ResourceType
    parent: _Event
