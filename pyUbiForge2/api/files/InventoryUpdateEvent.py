from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class InventoryUpdateEvent(SubclassBaseFile):
    ResourceType = 0xAEB5ABE2
    ParentResourceType = _Event.ResourceType
    parent: _Event

