from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class InventoryItemSettingsChangeEvent(SubclassBaseFile):
    ResourceType = 0xF661EC8A
    ParentResourceType = _Event.ResourceType
    parent: _Event
