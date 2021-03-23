from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class InventoryChangeEvent(SubclassBaseFile):
    ResourceType = 0xA552C09C
    ParentResourceType = _Event.ResourceType
    parent: _Event

