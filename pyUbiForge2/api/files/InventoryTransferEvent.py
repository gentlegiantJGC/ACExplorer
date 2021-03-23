from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class InventoryTransferEvent(SubclassBaseFile):
    ResourceType = 0xB2BC4010
    ParentResourceType = _Event.ResourceType
    parent: _Event

