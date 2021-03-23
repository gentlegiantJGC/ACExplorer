from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class LootEvent(SubclassBaseFile):
    ResourceType = 0x9FD03755
    ParentResourceType = _Event.ResourceType
    parent: _Event

